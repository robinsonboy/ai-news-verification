import os
import sys
# DON\'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.news import News, VerificationLog, NewsSource
from src.routes.user import user_bp
from src.routes.news import news_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# 啟用 CORS 支援
CORS(app, origins="*")

# 註冊藍圖
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(news_bp, url_prefix='/api')

# 資料庫配置
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 建立資料庫表格
with app.app_context():
    db.create_all()
    
    # 初始化一些預設的新聞來源
    if NewsSource.query.count() == 0:
        default_sources = [
            NewsSource(name='中央社', domain='cna.com.tw', credibility_score=90, bias_score=0, description='官方通訊社'),
            NewsSource(name='聯合新聞網', domain='udn.com', credibility_score=85, bias_score=5, description='主流媒體'),
            NewsSource(name='自由時報', domain='ltn.com.tw', credibility_score=80, bias_score=-10, description='主流媒體'),
            NewsSource(name='中國時報', domain='chinatimes.com', credibility_score=80, bias_score=10, description='主流媒體'),
            NewsSource(name='BBC', domain='bbc.com', credibility_score=95, bias_score=0, description='國際權威媒體'),
            NewsSource(name='Reuters', domain='reuters.com', credibility_score=95, bias_score=0, description='國際通訊社'),
        ]
        
        for source in default_sources:
            db.session.add(source)
        
        db.session.commit()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
