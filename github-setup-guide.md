# GitHub 專案建立指南

## 步驟 1：建立新的 GitHub 倉庫

1. 點擊綠色的 "New" 按鈕
2. 填寫倉庫資訊：
   - **Repository name**: `ai-news-verification`
   - **Description**: `AI 驅動的新聞驗證網站 - 100% 可信新聞平台`
   - **Visibility**: 選擇 Public（公開）或 Private（私人）
   - **Initialize this repository with**: 
     - ✅ Add a README file
     - ✅ Add .gitignore (選擇 Python 模板)
     - ✅ Choose a license (建議選擇 MIT License)

3. 點擊 "Create repository" 建立倉庫

## 步驟 2：準備上傳檔案

建立完倉庫後，您會看到一個空的專案頁面。接下來我們需要上傳專案檔案。

### 方法 A：使用 GitHub 網頁介面（推薦給初學者）

1. 點擊 "uploading an existing file" 連結
2. 將我提供的所有檔案拖拉到上傳區域
3. 填寫 commit 訊息：`Initial commit: AI news verification website`
4. 點擊 "Commit changes"

### 方法 B：使用 Git 命令列

```bash
git clone https://github.com/your-username/ai-news-verification.git
cd ai-news-verification
# 複製所有專案檔案到這個目錄
git add .
git commit -m "Initial commit: AI news verification website"
git push origin main
```

## 步驟 3：檔案結構

上傳完成後，您的倉庫應該包含以下檔案結構：

```
ai-news-verification/
├── README.md
├── .gitignore
├── LICENSE
├── backend/
│   ├── src/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── venv/ (這個目錄不會上傳到 GitHub)
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── node_modules/ (這個目錄不會上傳到 GitHub)
└── deployment/
    ├── vercel.json
    └── railway.json
```

## 步驟 4：設定部署

### Vercel 部署（推薦）

1. 前往 [vercel.com](https://vercel.com)
2. 使用 GitHub 帳號登入
3. 點擊 "New Project"
4. 選擇您剛建立的 `ai-news-verification` 倉庫
5. 設定環境變數：
   - `OPENAI_API_KEY`: 您的 OpenAI API 金鑰
   - `OPENAI_API_BASE`: `https://api.openai.com/v1`
6. 點擊 "Deploy"

### Railway 部署

1. 前往 [railway.app](https://railway.app)
2. 使用 GitHub 帳號登入
3. 點擊 "New Project"
4. 選擇 "Deploy from GitHub repo"
5. 選擇您的倉庫
6. 設定環境變數（同上）
7. Railway 會自動部署

## 步驟 5：測試部署

部署完成後，您會獲得一個公開的網址，例如：
- Vercel: `https://ai-news-verification.vercel.app`
- Railway: `https://ai-news-verification.up.railway.app`

訪問這個網址，您應該能看到完整的 AI 新聞驗證網站！

## 疑難排解

如果遇到問題，請檢查：
1. 環境變數是否正確設定
2. OpenAI API 金鑰是否有效
3. 部署日誌中是否有錯誤訊息

需要協助嗎？請在 GitHub Issues 中提出問題！

