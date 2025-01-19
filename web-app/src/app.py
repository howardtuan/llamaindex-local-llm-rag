from flask import Flask, render_template, request, jsonify
import os
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from LoadPathScript import load_json

app = Flask(__name__)

persist_dir = load_json("KG_db_path")
chroma_db_path = load_json("chroma_db_path")

print("伺服器已啟動，目前正在初始化，請稍等...")

# 初始化 ChromaDB 客户端
print("------------------------------------")
print("連線ChromaDB...")
print("如果chroma_db資料夾不存在，請先執行CreateChromaDB.py，否則伺服器會報錯！")
chroma_client = chromadb.PersistentClient(path=chroma_db_path)
chroma_collection = chroma_client.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
print("成功初始化ChromaDB客戶端！")
print("------------------------------------")
# 初始化嵌入模型和 LLM
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)

# 從 ChromaDB 創建 VectorStoreIndex
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context)
query_engine = index.as_query_engine()

def initialize_graph_rag():
    # 初始化嵌入模型和 LLM
    llm = Ollama(model="llama3.1", request_timeout=120.0)
    print("連線KG圖譜DB...")
    print("如果storage資料夾不存在，請先執行CreateGraphRagDB.py，否則伺服器會報錯！")
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    graph_index = load_index_from_storage(storage_context)
    print("載入成功！")  
    print("------------------------------------")  
    return graph_index.as_query_engine(llm=llm, similarity_top_k=5)

# 初始化 Graph RAG 查询引擎
graph_query_engine = initialize_graph_rag()

print("伺服器正式啟動！")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query_text = data['question']
    response = query_engine.query(query_text)
    result = {
        "response": response.response
    }
    return jsonify(result)

@app.route('/graph-rag', methods=['POST'])
def graph_rag():
    data = request.get_json()
    query_text = data['question']
    response = graph_query_engine.query(query_text)
    result = {
        "response": response.response
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
