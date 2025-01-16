import os
import chromadb
from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex, StorageContext, load_index_from_storage, Settings,VectorStoreIndex,Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
# 配置路径
persist_dir = os.path.abspath("./storage")
chroma_db_path = os.path.abspath("./chroma_db")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)
def update_chroma_db(new_docs_path, collection_name="quickstart"):
    if not os.path.exists(new_docs_path):
        print(f"目錄 {new_docs_path} 不存在！")
        return

    # 初始化 ChromaDB 客户端和集合
    db = chromadb.PersistentClient(path=chroma_db_path)
    chroma_collection = db.get_or_create_collection(collection_name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 加载新文档
    documents = SimpleDirectoryReader(new_docs_path).load_data()
    if not documents:
        print(f"目錄 {new_docs_path} 中没有可用的文件！")
        return

    # 初始化嵌入模型
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    # 创建新的索引并更新到 ChromaDB
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model)
  

    print(f"成功將 {len(documents)} 個新文件導入至ChromaDB的collection: {collection_name}")


def update_knowledge_graph(new_docs_path):
    if not os.path.exists(new_docs_path):
        print(f"目錄 {new_docs_path} 不存在！")
        return

    # 加载新文档
    raw_documents = SimpleDirectoryReader(new_docs_path).load_data()
    if not raw_documents:
        print(f"目錄 {new_docs_path} 中沒有可用的文件！")
        return

    new_documents = [
        Document(text=doc.text, metadata=doc.metadata, doc_id=doc.metadata.get("doc_id", f"doc_{i}"))
        for i, doc in enumerate(raw_documents)
    ]

    try:
        if os.path.exists(persist_dir):
            print("persist_dir:", persist_dir)
            print("載入現有 KnowledgeGraphIndex...")
            storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
            graph_index = load_index_from_storage(storage_context)
        else:
            print("未找到索引，重新初始化...")
            storage_context = StorageContext.from_defaults()
            graph_index = KnowledgeGraphIndex.from_documents(
                documents=[],  # 初始为空
                max_triplets_per_chunk=3,
                storage_context=storage_context,
                llm=Settings.llm,
                embed_model=Settings.embed_model,
                include_embeddings=True
            )
            print("索引初始化完成！")

        # 更新索引
        print(f"更新索引，新增文件數: {len(new_documents)}")
        for doc in new_documents:
            graph_index.update_ref_doc(doc)  # 调用 update_ref_doc 更新文档

        # 保存更新后的索引
        graph_index.storage_context.persist(persist_dir=persist_dir)
        print("索引已成功更新并保存！")


    except Exception as e:
        print(f"更新 KnowledgeGraphIndex 失败: {e}")




if __name__ == "__main__":
    # ChromaDB 可以正常匯入新資料，但是KnowledgeGraphIndex可能會有bug，但可以確認的是它會新增在storage資料夾

    new_docs_path = "C:\\Users\\howar\\OneDrive\\桌面\\RAG_Project_withUI_test\\web-app\\src\\MyMD_New"
    print("\n開始更新 ChromaDB...")
    update_chroma_db(new_docs_path)

    print("\n開始更新 KnowledgeGraphIndex...")
    update_knowledge_graph(new_docs_path)

