from src.models.user import db
from datetime import datetime
import json

class News(db.Model):
    """新聞資料模型"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(500), unique=True, nullable=True)
    source = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # AI 驗證相關欄位
    verification_status = db.Column(db.String(50), default=r'pending')  # pending, reviewing, verified, fake, questionable
    credibility_score = db.Column(db.Integer, nullable=True)  # 0-100
    ai_analysis_results = db.Column(db.Text, nullable=True)  # JSON 格式儲存 AI 分析的詳細結果

    # 關聯到驗證日誌
    verification_logs = db.relationship(\'VerificationLog\', backref=\'news\', lazy=True)

    def to_dict(self):
        return {
            \'id\': self.id,
            \'title\': self.title,
            \'content\': self.content,
            \'url\': self.url,
            \'source\': self.source,
            \'category\': self.category,
            \'published_at\': self.published_at.isoformat() + \'Z\' if self.published_at else None,
            \'created_at\': self.created_at.isoformat() + \'Z\',
            \'updated_at\': self.updated_at.isoformat() + \'Z\',
            \'verification_status\': self.verification_status,
            \'credibility_score\': self.credibility_score,
            \'ai_analysis_results\': json.loads(self.ai_analysis_results) if self.ai_analysis_results else None
        }

class VerificationLog(db.Model):
    """新聞驗證日誌模型"""
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey(\'news.id\'), nullable=False)
    verifier = db.Column(db.String(100), default=\'AI\')  # AI 或人工審核員名稱
    status_before = db.Column(db.String(50), nullable=True)
    status_after = db.Column(db.String(50), nullable=False)
    score_before = db.Column(db.Integer, nullable=True)
    score_after = db.Column(db.Integer, nullable=True)
    reason = db.Column(db.Text, nullable=True)
    verified_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            \'id\': self.id,
            \'news_id\': self.news_id,
            \'verifier\': self.verifier,
            \'status_before\': self.status_before,
            \'status_after\': self.status_after,
            \'score_before\': self.score_before,
            \'score_after\': self.score_after,
            \'reason\': self.reason,
            \'verified_at\': self.verified_at.isoformat() + \'Z\'
        }

class NewsSource(db.Model):
    """新聞來源模型"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    domain = db.Column(db.String(255), unique=True, nullable=False)
    credibility_score = db.Column(db.Integer, default=50) # 0-100
    bias_score = db.Column(db.Integer, default=0) # -100 (左傾) 到 100 (右傾)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            \'id\': self.id,
            \'name\': self.name,
            \'domain\': self.domain,
            \'credibility_score\': self.credibility_score,
            \'bias_score\': self.bias_score,
            \'description\': self.description,
            \'created_at\': self.created_at.isoformat() + \'Z\',
            \'updated_at\': self.updated_at.isoformat() + \'Z\'
        }

