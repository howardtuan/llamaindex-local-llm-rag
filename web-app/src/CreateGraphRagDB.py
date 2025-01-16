import os
from llama_index.core import KnowledgeGraphIndex, StorageContext,Settings
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.core import SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 文件路徑
documents_path = "MD文件資料夾位置"
persist_dir = os.path.abspath("./storage")

# 初始化 LLM 和嵌入模型
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)
llm = Ollama(model="llama3.1", request_timeout=120.0)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

def create_graph_rag():
    print("初始化KG資料...")

    # 創建一個 SimpleGraphStore 和儲存上下文
    graph_store = SimpleGraphStore()
    storage_context = StorageContext.from_defaults(graph_store=graph_store)

    # 載入文件
    documents = SimpleDirectoryReader(documents_path).load_data()

    # 創建 KnowledgeGraphIndex
    graph_index = KnowledgeGraphIndex.from_documents(
        documents=documents,
        max_triplets_per_chunk=3,
        storage_context=storage_context,
        llm=llm,
        embed_model=embed_model,
        include_embeddings=True
    )

    # 創建永久目錄
    os.makedirs(persist_dir, exist_ok=True)

    # 存檔
    graph_index.storage_context.persist(persist_dir=persist_dir)
    print("KG圖譜儲存並建立成功！")

if __name__ == "__main__":
    print("執行此腳本前記得先跑過PDF2MD.py，確保有MD文件，並儲存在指定資料夾中！")
    create_graph_rag()
