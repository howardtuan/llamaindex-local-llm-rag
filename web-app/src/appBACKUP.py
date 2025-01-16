from flask import Flask, render_template, request, jsonify
import os
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import KnowledgeGraphIndex
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.core import SimpleDirectoryReader

app = Flask(__name__)
persist_dir = os.path.abspath("./storage")
chroma_db_path = os.path.abspath("./chroma_db")

# 初始化 ChromaDB 客户端
chroma_client = chromadb.PersistentClient(path=chroma_db_path)
chroma_collection = chroma_client.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 初始化嵌入模型和 LLM
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)

# 从 ChromaDB 创建 VectorStoreIndex
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context)
query_engine = index.as_query_engine()

# 文档路径
documents_path = "C:\\Users\\howar\\OneDrive\\桌面\\RAG_Project_withUI_test\\web-app\\src\\MyMD_temp"



def initialize_graph_rag():
    # 初始化嵌入模型和 LLM
    llm = Ollama(model="llama3.1", request_timeout=120.0)
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    
    # 检查持久化目录是否存在
    if os.path.exists(persist_dir):
        print("从存储加载索引...")
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        graph_index = load_index_from_storage(storage_context)
        print("索引加载成功！")
    else:
        print("存储中未找到索引，重新初始化...")
        graph_store = SimpleGraphStore()
        storage_context = StorageContext.from_defaults(graph_store=graph_store)
        
        # 加载文档
        documents = SimpleDirectoryReader(documents_path).load_data()
        
        # 创建 KnowledgeGraphIndex
        graph_index = KnowledgeGraphIndex.from_documents(
            documents=documents,
            max_triplets_per_chunk=3,
            storage_context=storage_context,
            llm=llm,
            embed_model=embed_model,
            include_embeddings=True
        )
        
        # 创建持久化目录
        os.makedirs(persist_dir, exist_ok=True)
        
        # 保存索引到存储
        graph_index.storage_context.persist(persist_dir=persist_dir)
        print("索引已保存到存储！")
    
    # 无论索引是加载还是创建，都需要返回 query_engine
    return graph_index.as_query_engine(llm=llm, similarity_top_k=5)


# 初始化 Graph RAG 查询引擎
graph_query_engine = initialize_graph_rag()

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
