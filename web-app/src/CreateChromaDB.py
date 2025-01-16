import chromadb
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader,StorageContext,VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore

def import_documents_to_chroma(directory, collection_name="quickstart"):
    print("初始化ChromaDB客戶端...")
    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("quickstart")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    documents = SimpleDirectoryReader(directory).load_data()
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model)
    print(f"成功輸入 {len(documents)} 個文件至ChromaDB的collection中: {collection_name}")


if __name__ == "__main__":
    print("執行此腳本前記得先跑過PDF2MD.py，確保有MD文件，並儲存在指定資料夾中！")
    directory = "MD文件資料夾位置"
    import_documents_to_chroma(directory)
