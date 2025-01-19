import json

def load_json(key, file_path="C:\\Users\\howar\\OneDrive\\桌面\\llamaindex-local-llm-rag\\web-app\\src\\Config.json"):
    """
    從 JSON 中載入指定的內容
    """
    with open(file_path, "r", encoding="utf-8") as file:
        config = json.load(file)
        return config.get(key)

