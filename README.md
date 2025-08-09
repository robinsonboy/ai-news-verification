# AI 新聞驗證網站

> 運用先進的人工智慧技術，為每一則新聞進行全面驗證，確保您獲得最可靠、最準確的資訊。

## 🚀 專案特色

- **🤖 AI 驗證技術** - 整合 OpenAI GPT-4 進行多維度新聞分析
- **📊 即時統計** - 提供驗證統計和趨勢分析
- **🔍 事實查核** - 與權威資料庫交叉驗證新聞內容
- **📱 響應式設計** - 支援桌面、平板、手機等各種裝置
- **⚡ 快速驗證** - 平均 30 秒內完成新聞可信度分析
- **🎯 準確評分** - 0-100 分的精確可信度評分系統

## 🎯 核心功能

### AI 驗證系統
- **事實查核** - 分析新聞內容的事實準確性
- **來源分析** - 評估新聞來源的可信度和歷史記錄
- **語言分析** - 檢測情緒化用詞、偏見指標和專業性
- **綜合評分** - 多維度加權計算最終可信度分數

### 用戶功能
- **新聞瀏覽** - 分類瀏覽已驗證的新聞
- **搜尋功能** - 快速搜尋特定主題新聞
- **提交驗證** - 用戶可提交新聞連結或內容進行驗證
- **統計儀表板** - 查看驗證統計和趨勢分析

### 驗證狀態
- ✅ **已驗證** - 高可信度新聞（80+ 分）
- ⚠️ **審核中** - 需要進一步驗證（60-79 分）
- ❓ **可疑** - 可信度較低（40-59 分）
- ❌ **疑似假新聞** - 低可信度（< 40 分）

## 🛠 技術架構

### 後端技術
- **Flask** - Python Web 框架
- **SQLAlchemy** - 資料庫 ORM
- **OpenAI API** - AI 分析服務
- **BeautifulSoup** - 網頁內容爬取
- **SQLite/PostgreSQL** - 資料庫

### 前端技術
- **React** - 用戶介面框架
- **Tailwind CSS** - 樣式框架
- **shadcn/ui** - UI 元件庫
- **Lucide Icons** - 圖標庫
- **Vite** - 建置工具

### 部署技術
- **Docker** - 容器化部署
- **Vercel/Railway** - 雲端部署平台
- **GitHub Actions** - CI/CD 自動化

## 📦 快速開始

### 環境需求
- Python 3.11+
- Node.js 18+
- OpenAI API Key

### 本地開發

1. **克隆專案**
```bash
git clone https://github.com/your-username/ai-news-verification.git
cd ai-news-verification
```

2. **後端設定**
```bash
cd ai_news_backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **環境變數設定**
```bash
cp .env.example .env
# 編輯 .env 檔案，添加您的 OpenAI API Key
```

4. **啟動後端**
```bash
python src/main.py
```

5. **前端設定**
```bash
cd ai-news-frontend
pnpm install
pnpm run dev
```

6. **訪問應用程式**
- 前端：http://localhost:5173
- 後端 API：http://localhost:5001

### 一鍵部署

#### Vercel 部署
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/ai-news-verification)

#### Railway 部署
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/your-username/ai-news-verification)

## 🔧 配置說明

### 環境變數
```env
# OpenAI API 設定
OPENAI_API_KEY=your_openai_api_key_here

# Flask 設定
FLASK_ENV=production
SECRET_KEY=your_secret_key_here

# 資料庫設定
DATABASE_URL=sqlite:///app.db  # 開發環境
# DATABASE_URL=postgresql://user:pass@host:port/db  # 生產環境
```

### API 端點

#### 新聞相關
- `GET /api/news` - 獲取新聞列表
- `GET /api/news/{id}` - 獲取新聞詳情
- `POST /api/news/submit` - 提交新聞驗證
- `POST /api/news/{id}/verify` - 重新驗證新聞

#### 統計相關
- `GET /api/statistics` - 獲取統計數據
- `GET /api/sources` - 獲取新聞來源列表

## 📊 系統架構圖

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React 前端    │────│   Flask 後端    │────│   OpenAI API    │
│                 │    │                 │    │                 │
│ • 新聞展示      │    │ • AI 驗證服務   │    │ • GPT-4 分析    │
│ • 用戶介面      │    │ • 新聞爬取      │    │ • 事實查核      │
│ • 統計圖表      │    │ • 資料庫管理    │    │ • 語言分析      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │
         │              ┌─────────────────┐
         └──────────────│   SQLite/PG     │
                        │                 │
                        │ • 新聞資料      │
                        │ • 驗證結果      │
                        │ • 來源資訊      │
                        └─────────────────┘
```

## 🎨 介面預覽

### 首頁
- 英雄區塊展示統計數據
- 最新驗證新聞列表
- 分類新聞區塊

### 新聞詳情頁
- 完整新聞內容
- AI 驗證結果詳情
- 可信度分數和分析
- 相關新聞推薦

### 提交驗證頁
- URL 提交表單
- 直接內容提交
- 即時驗證狀態

## 🔒 安全特性

- **HTTPS 強制** - 所有連接均使用 SSL 加密
- **API 金鑰保護** - 環境變數安全儲存
- **輸入驗證** - 防止 XSS 和注入攻擊
- **速率限制** - 防止 API 濫用
- **CORS 設定** - 跨域請求安全控制

## 📈 效能優化

- **前端優化**
  - 程式碼分割和懶載入
  - 圖片壓縮和 CDN
  - 快取策略

- **後端優化**
  - 資料庫索引優化
  - API 回應快取
  - 非同步處理

## 🤝 貢獻指南

1. Fork 專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 📞 聯絡資訊

- **專案連結**: [https://github.com/your-username/ai-news-verification](https://github.com/your-username/ai-news-verification)
- **線上 Demo**: [https://ai-news-verify.vercel.app](https://ai-news-verify.vercel.app)
- **問題回報**: [GitHub Issues](https://github.com/your-username/ai-news-verification/issues)

## 🙏 致謝

- [OpenAI](https://openai.com) - 提供強大的 AI 分析能力
- [React](https://reactjs.org) - 優秀的前端框架
- [Flask](https://flask.palletsprojects.com) - 簡潔的 Python Web 框架
- [Tailwind CSS](https://tailwindcss.com) - 實用的 CSS 框架

---

**⭐ 如果這個專案對您有幫助，請給我們一個 Star！**

