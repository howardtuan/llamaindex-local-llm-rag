# 基於 LlamaIndex 和地端 LLM 的自然語言查詢系統
本專案是一個基於 LlamaIndex 框架和地端 LLM (大型語言模型)的自然語言查詢系統。

## 使用的技術
LlamaIndex: 轉換和編排文件，幫助快速建構知識架構和問答模型。<br>
地端 LLM: Ollama llama3.1:8b 模型<br>
ChromaDB: 基於向量儲存的資料庫。

## 功能特色
完整知識文件導入：支援 Markdown (☆.md)和其他文件格式(以純文字為主)。<br>
基於知識圖譜的自然語言問答能力。<br>
地端語言生成，保障資料隱私。<br>
允許加入新文件並自動更新知識圖與向量資料庫。

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
ChromaDB: 用來儲存向量資料。<br>
KnowledgeGraphIndex: 知識圖儲存與問答模型。<br>
Storage Context: 記得確保 Flask 和項目自動更新這些儲存路徑。

## 常見問題 (FAQ)
Q:語言模型無法回應？<br>
A:確保您的 Ollama 模型已正確安裝，且服務已啟動。本專案的LLM是llama 3.1:8b<br>

Q:路徑不正確導致儲存失敗？<br>
A:確保設定的 persist_dir 和 chroma_db_path 是一致的。<br>
