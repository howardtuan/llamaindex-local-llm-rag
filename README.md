# 基於 LlamaIndex 和地端 LLM 的自然語言查詢系統

此專案是一個網頁應用程式，允許使用者輸入問題並接收來自 ChromaDB 或 知識圖譜 的查詢結果以及來自語言模型 (LLM) 的回應。該應用程式使用 Flask 構建，並整合了 LlamaIndex 框架以進行文件檢索和 LLM 生成回應。

## 專案結構

```
llamaindex-local-llm-rag/
|
├──web-app/
│  └── src/
│      ├── app.py                 # 網頁應用程式的主要入口
│      ├── appBACKUP.py           # 舊版Flask後端備份
│      ├── CreateChromaDB.py      # 初始化與建立ChromaDB
│      ├── CreateGraphRagDB.py    # 初始化與建立知識圖譜
│      ├── InsertNewMD.py         # 輸入MD檔案至ChromaDB與知識圖譜
│      ├── PDF2MD.py              # 將PDF檔案轉至MD
│      │── templates
│      │   └── index.html         # 用戶界面的 HTML 模板
│      │── MyMD_temp
│      │   └── original.MD        # 原始MD檔案
│      └── MyMD_New
│          └── new.MD             # 新的MD檔案(未來新增用的路徑)
├──chroma_db/
│  └── some_default_files         # chroma_db預設儲存的內容(已事先將 MyMD_temp 與 MyMD_New 匯入)
├──storage
│  └── some_default_files         # storage預設儲存的內容(已事先將 MyMD_temp 與 MyMD_New 匯入)
├── requirements.txt              # 列出專案必要套件
└── README.md                     # 專案文件
```

## 設置說明

1. **建立儲存庫**：
   ```
   git clone https://github.com/howardtuan/llamaindex-local-llm-rag.git
   cd web-app
   ```
2. **安裝必要套件**：<br>
   建議使用虛擬環境。您可以使用以下指令創建一個虛擬環境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
   ```
   然後安裝所需的套件：
   ```
   pip install -r requirements.txt
   ```
3. **前置作業**：
   - 若只想先測試的話可以直接進入`第4點`啟動伺服器
   - run `PDF2MD.py` : 將PDF文件轉成MD格式，並儲存在指定目錄(你也可以放txt文件)
   - run `CreateChromaDB.py` : 建立以及初始化ChromaDB
   - run `CreateGraphRagDB.py` : 建立以及初始化知識圖譜
   - 未來若有需要新增資料 run `InsertNewMD.py` : 新增MD檔案至ChromaDB與知識圖譜

4. **運行應用程式**：<br>
   請事先安裝`ollama`，並執行 `ollama pull llama3.1`<br>
   通過運行以下命令啟動 Flask 應用程式：
   ```
   python src/app.py
   ```
   應用程式將可在 `http://127.0.0.1:5000` 訪問。

## 使用指南

- 打開您的網頁瀏覽器並導航到應用程式 URL。
- 在提供的表單中輸入您的問題並提交。
- 應用程式將使用 LlamaIndex 查詢 ChromaDB 或 知識圖譜 以獲取相關文件，並使用 LLM 生成回應。

## 使用的技術
- LlamaIndex: 轉換和編排文件，幫助快速建構知識架構和問答模型。
- 地端 LLM: Ollama llama3.1:8b 模型
- ChromaDB: 基於向量儲存的資料庫。

## 功能特色
- 完整知識文件導入：支援 Markdown (☆.md)和其他文件格式(以純文字為主)。
- 基於知識圖譜的自然語言問答能力。
- 地端語言生成，保障資料隱私。
- 允許加入新文件並自動更新知識圖與向量資料庫。

## API 參考
#### /ask
* 使用 VectorStoreIndex 來進行問答。
* 參數：
    ```JSON
    {
        "question": "What is btc etf affect the market"
    }
    ```
    ```JSON
    {
        "response": "BTC ETF..."
    }
    ```
#### /graph-rag
* 使用 KnowledgeGraphIndex 來進行問答。
* 參數：
    ```JSON
    {
        "question": "what is Enhanced-TransUnet?"
    }
    ```
    ```JSON
    {
        "response": "Enhanced-TransUnet is a ..."
    }
    ```
## 資料儲存
- ChromaDB: 用來儲存向量資料。
- KnowledgeGraphIndex: 知識圖儲存與問答模型。
- Storage Context: 記得確保 Flask 和項目自動更新這些儲存路徑。

## 常見問題 (FAQ)
Q : 語言模型無法回應？<br>
A : 確保您的 Ollama 模型已正確安裝，且服務已啟動。本專案的LLM是llama 3.1:8b<br>

Q : 路徑不正確導致儲存失敗？<br>
A : 確保設定的 persist_dir 和 chroma_db_path 是一致的。<br>
