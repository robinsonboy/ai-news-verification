import os
import requests
from openai import OpenAI
from bs4 import BeautifulSoup
import json

class AIVerificationService:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def verify_news(self, title, content, source=None, url=None):
        # 模擬 AI 驗證過程
        # 實際應用中會調用 OpenAI API 進行複雜分析
        
        credibility_score = self._calculate_mock_credibility(title, content, source)
        verification_status = self._determine_status(credibility_score)
        
        ai_analysis_results = {
            "fact_check_summary": "這是一個模擬的事實查核摘要。",
            "source_analysis": f"來源 {source} 的可信度分析摘要。",
            "language_analysis": "語言分析顯示文本語氣中立，無明顯煽動性詞語。",
            "bias_indicators": "模擬偏見指標：無明顯偏見。",
            "keywords": ["AI", "新聞", "驗證", "模擬"]
        }

        return {
            "verification_status": verification_status,
            "credibility_score": credibility_score,
            "ai_analysis_results": json.dumps(ai_analysis_results)
        }

    def _calculate_mock_credibility(self, title, content, source):
        # 根據標題、內容和來源模擬可信度分數
        score = 70 # 基礎分數

        if "假消息" in title or "澄清" in title or "闢謠" in title:
            score -= 30
        if "AI" in title or "科技" in title:
            score += 5
        
        if source and ("中央社" in source or "BBC" in source or "Reuters" in source):
            score += 15
        elif source and ("娛樂" in source or "八卦" in source):
            score -= 20
            
        if len(content) < 100:
            score -= 10 # 內容過短可能可信度低

        return max(0, min(100, score))

    def _determine_status(self, score):
        if score >= 85:
            return "verified"
        elif score >= 60:
            return "reviewing"
        elif score >= 40:
            return "questionable"
        else:
            return "fake"

class NewsCrawlerService:
    def fetch_and_parse(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status() # 檢查 HTTP 錯誤
            soup = BeautifulSoup(response.text, 'html.parser')

            title = self._extract_title(soup)
            content = self._extract_content(soup)
            source = self._extract_source(url)
            published_at = self._extract_published_at(soup)

            return {
                "title": title,
                "content": content,
                "source": source,
                "published_at": published_at,
                "url": url
            }
        except requests.exceptions.RequestException as e:
            print(f"爬取或解析失敗: {e}")
            return None

    def _extract_title(self, soup):
        # 嘗試從常見的標籤中提取標題
        title_tags = ["h1", "title", "meta[property=\"og:title\"]", "meta[name=\"twitter:title\"]"]
        for tag in title_tags:
            element = soup.select_one(tag)
            if element:
                if tag.startswith("meta"):
                    return element.get("content")
                return element.get_text(strip=True)
        return "無標題"

    def _extract_content(self, soup):
        # 嘗試從常見的內容標籤中提取內容
        content_tags = ["article", "div.content", "div.article-body", "div.entry-content", "div.post-content"]
        for tag in content_tags:
            element = soup.select_one(tag)
            if element:
                paragraphs = element.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li"])
                return "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
        return "無內容"

    def _extract_source(self, url):
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        return parsed_url.netloc.replace("www.", "")

    def _extract_published_at(self, soup):
        # 嘗試從常見的日期時間標籤中提取發布時間
        date_tags = ["time", "meta[property=\"article:published_time\"]", "meta[name=\"pubdate\"]"]
        for tag in date_tags:
            element = soup.select_one(tag)
            if element:
                if tag.startswith("meta"):
                    date_str = element.get("content")
                else:
                    date_str = element.get("datetime") or element.get_text(strip=True)
                
                try:
                    # 嘗試解析多種日期格式
                    from dateutil.parser import parse
                    return parse(date_str)
                except Exception:
                    pass
        return None


