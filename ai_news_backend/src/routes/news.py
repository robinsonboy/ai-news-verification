from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.news import News, VerificationLog, NewsSource
from src.services.ai_verification import AIVerificationService, NewsCrawlerService
from sqlalchemy import desc

news_bp = Blueprint(\'news\', __name__)

ai_verifier = AIVerificationService()
news_crawler = NewsCrawlerService()

@news_bp.route(\'/news\', methods=[\'GET\'])
def get_news():
    page = request.args.get(\'page\', 1, type=int)
    per_page = request.args.get(\'per_page\', 10, type=int)
    category = request.args.get(\'category\', type=str)
    status = request.args.get(\'status\', type=str)
    search_query = request.args.get(\'search\', type=str)

    query = News.query

    if category:
        query = query.filter_by(category=category)
    if status:
        query = query.filter_by(verification_status=status)
    if search_query:
        query = query.filter(News.title.contains(search_query) | News.content.contains(search_query))

    pagination = query.order_by(desc(News.published_at)).paginate(
        page=page, per_page=per_page, error_out=False
    )

    news_items = [news.to_dict() for news in pagination.items]

    return jsonify({
        \"success\": True,
        \"data\": {
            \"news\": news_items,
            \"pagination\": {
                \"total\": pagination.total,
                \"page\": pagination.page,
                \"per_page\": pagination.per_page,
                \"pages\": pagination.pages,
                \"has_next\": pagination.has_next,
                \"has_prev\": pagination.has_prev
            }
        }
    })

@news_bp.route(\'/news/<int:news_id>\', methods=[\'GET\'])
def get_news_detail(news_id):
    news = News.query.get_or_404(news_id)
    return jsonify({\"success\": True, \"data\": news.to_dict()})

@news_bp.route(\'/news/submit\', methods=[\'POST\'])
def submit_news():
    data = request.get_json()
    url = data.get(\'url\')
    title = data.get(\'title\')
    content = data.get(\'content\')
    source = data.get(\'source\')
    published_at = data.get(\'published_at\')

    if url:
        # 如果提供了 URL，嘗試爬取內容
        crawled_data = news_crawler.fetch_and_parse(url)
        if not crawled_data:
            return jsonify({\"success\": False, \"message\": \"無法爬取新聞內容或解析失敗\"}), 400
        title = crawled_data.get(\'title\')
        content = crawled_data.get(\'content\')
        source = crawled_data.get(\'source\')
        published_at = crawled_data.get(\'published_at\')
    elif not (title and content and source):
        return jsonify({\"success\": False, \"message\": \"請提供新聞標題、內容和來源，或提供新聞 URL\"}), 400

    # 檢查新聞是否已存在
    existing_news = News.query.filter_by(url=url).first() if url else None
    if existing_news:
        return jsonify({\"success\": False, \"message\": \"新聞已存在\", \"data\": existing_news.to_dict()}), 409

    # 進行 AI 驗證
    verification_results = ai_verifier.verify_news(title, content, source, url)

    new_news = News(
        title=title,
        content=content,
        url=url,
        source=source,
        category=\'general\', # 預設分類，可後續擴展 AI 分類功能
        published_at=published_at,
        verification_status=verification_results[\"verification_status\"],
        credibility_score=verification_results[\"credibility_score\"],
        ai_analysis_results=verification_results[\"ai_analysis_results\"]
    )

    db.session.add(new_news)
    db.session.commit()

    # 記錄驗證日誌
    log = VerificationLog(
        news_id=new_news.id,
        status_after=new_news.verification_status,
        score_after=new_news.credibility_score,
        reason=\"首次 AI 驗證\"
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({\"success\": True, \"message\": \"新聞已提交並完成初步 AI 驗證\", \"data\": new_news.to_dict()}), 200

@news_bp.route(\'/news/<int:news_id>/verify\', methods=[\'POST\'])
def reverify_news(news_id):
    news = News.query.get_or_404(news_id)

    status_before = news.verification_status
    score_before = news.credibility_score

    # 重新進行 AI 驗證
    verification_results = ai_verifier.verify_news(news.title, news.content, news.source, news.url)

    news.verification_status = verification_results[\"verification_status\"]
    news.credibility_score = verification_results[\"credibility_score\"]
    news.ai_analysis_results = verification_results[\"ai_analysis_results\"]
    news.updated_at = datetime.utcnow()

    db.session.commit()

    # 記錄驗證日誌
    log = VerificationLog(
        news_id=news.id,
        status_before=status_before,
        status_after=news.verification_status,
        score_before=score_before,
        score_after=news.credibility_score,
        reason=\"重新 AI 驗證\"
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({\"success\": True, \"message\": \"新聞已重新驗證\", \"data\": news.to_dict()})

@news_bp.route(\'/statistics\', methods=[\'GET\'])
def get_statistics():
    total_news = News.query.count()
    verified_news = News.query.filter_by(verification_status=\'verified\').count()
    fake_news = News.query.filter_by(verification_status=\'fake\').count()
    pending_news = News.query.filter_by(verification_status=\'pending\').count()
    reviewing_news = News.query.filter_by(verification_status=\'reviewing\').count()
    questionable_news = News.query.filter_by(verification_status=\'questionable\').count()

    verification_rate = (verified_news / total_news * 100) if total_news > 0 else 0

    return jsonify({
        \"success\": True,
        \"data\": {
            \"overview\": {
                \"total_news\": total_news,
                \"verified_news\": verified_news,
                \"fake_news\": fake_news,
                \"pending_news\": pending_news,
                \"reviewing_news\": reviewing_news,
                \"questionable_news\": questionable_news,
                \"verification_rate\": round(verification_rate, 2)
            }
        }
    })

@news_bp.route(\'/sources\', methods=[\'GET\'])
def get_sources():
    sources = NewsSource.query.all()
    return jsonify({\"success\": True, \"data\": [s.to_dict() for s in sources]})

