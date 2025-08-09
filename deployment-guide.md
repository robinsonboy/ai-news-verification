# 🚀 AI 新聞驗證網站部署指南

## 📋 部署前準備

### 1. 獲取 OpenAI API 金鑰

1. 前往 [OpenAI Platform](https://platform.openai.com)
2. 註冊或登入帳號
3. 前往 API Keys 頁面
4. 點擊 "Create new secret key"
5. 複製並安全保存您的 API 金鑰

### 2. 確認專案檔案

確保您的 GitHub 倉庫包含以下檔案：
- `README.md`
- `.gitignore`
- `vercel.json`
- `ai_news_backend/` 目錄（包含所有後端檔案）
- `ai-news-frontend/` 目錄（包含所有前端檔案）

## 🌐 Vercel 部署（推薦）

### 步驟 1：連接 GitHub

1. 前往 [vercel.com](https://vercel.com)
2. 點擊 "Sign up" 或 "Log in"
3. 選擇 "Continue with GitHub"
4. 授權 Vercel 存取您的 GitHub 帳號

### 步驟 2：建立新專案

1. 在 Vercel 儀表板點擊 "New Project"
2. 從 GitHub 倉庫列表中選擇 `ai-news-verification`
3. 點擊 "Import"

### 步驟 3：配置專案設定

**Framework Preset**: 選擇 "Other"

**Root Directory**: 保持預設（./）

**Build and Output Settings**:
- Build Command: `cd ai-news-frontend && npm install && npm run build && cp -r dist/* ../ai_news_backend/src/static/`
- Output Directory: `ai_news_backend`
- Install Command: `cd ai_news_backend && pip install -r requirements.txt`

### 步驟 4：設定環境變數

在 "Environment Variables" 區域新增：

| Name | Value |
|------|-------|
| `OPENAI_API_KEY` | 您的 OpenAI API 金鑰 |
| `OPENAI_API_BASE` | `https://api.openai.com/v1` |

### 步驟 5：部署

1. 點擊 "Deploy"
2. 等待部署完成（通常需要 2-5 分鐘）
3. 部署成功後，您會獲得一個公開網址

## 🚂 Railway 部署

### 步驟 1：建立 Railway 專案

1. 前往 [railway.app](https://railway.app)
2. 使用 GitHub 帳號登入
3. 點擊 "New Project"
4. 選擇 "Deploy from GitHub repo"

### 步驟 2：選擇倉庫

1. 選擇您的 `ai-news-verification` 倉庫
2. 點擊 "Deploy Now"

### 步驟 3：設定環境變數

1. 在專案儀表板中點擊 "Variables"
2. 新增以下變數：
   - `OPENAI_API_KEY`: 您的 OpenAI API 金鑰
   - `OPENAI_API_BASE`: `https://api.openai.com/v1`

### 步驟 4：配置部署

Railway 會自動偵測 Python 專案並開始部署。如果需要自定義：

1. 建立 `railway.json` 檔案：
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "cd ai_news_backend && python src/main.py",
    "healthcheckPath": "/api/statistics"
  }
}
```

## 🔧 Render 部署

### 步驟 1：建立 Render 服務

1. 前往 [render.com](https://render.com)
2. 使用 GitHub 帳號註冊/登入
3. 點擊 "New +" → "Web Service"

### 步驟 2：連接倉庫

1. 選擇您的 GitHub 倉庫
2. 填寫服務資訊：
   - **Name**: `ai-news-verification`
   - **Environment**: `Python 3`
   - **Build Command**: `cd ai-news-frontend && npm install && npm run build && cp -r dist/* ../ai_news_backend/src/static/ && cd ../ai_news_backend && pip install -r requirements.txt`
   - **Start Command**: `cd ai_news_backend && python src/main.py`

### 步驟 3：設定環境變數

在 "Environment" 區域新增：
- `OPENAI_API_KEY`
- `OPENAI_API_BASE`

## 📱 手機版測試

部署完成後，請在不同裝置上測試：

1. **桌面瀏覽器**：Chrome、Firefox、Safari
2. **手機瀏覽器**：iOS Safari、Android Chrome
3. **平板**：iPad、Android 平板

## 🐛 疑難排解

### 常見問題

**1. 部署失敗：找不到模組**
- 確認 `requirements.txt` 包含所有必要的 Python 套件
- 檢查 `package.json` 是否包含所有 Node.js 依賴

**2. API 錯誤：OpenAI 金鑰無效**
- 確認環境變數 `OPENAI_API_KEY` 設定正確
- 檢查 OpenAI 帳號是否有足夠的額度

**3. 前端無法載入**
- 確認前端建置檔案已正確複製到 `ai_news_backend/src/static/`
- 檢查 Flask 路由是否正確設定

**4. 資料庫錯誤**
- SQLite 資料庫會在首次運行時自動建立
- 確認應用程式有寫入權限

### 檢查部署狀態

訪問以下端點來檢查服務狀態：
- `https://your-domain.com/api/statistics` - 應該返回統計數據
- `https://your-domain.com/api/news` - 應該返回新聞列表（可能為空）

## 🎉 部署成功！

恭喜！您的 AI 新聞驗證網站現在已經上線了。

**下一步：**
1. 測試新聞提交功能
2. 邀請朋友試用
3. 監控 API 使用量
4. 根據需要調整 AI 驗證邏輯

**需要協助？**
- 查看部署平台的日誌
- 在 GitHub Issues 中提出問題
- 參考官方文檔

