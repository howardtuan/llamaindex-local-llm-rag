import os
from markitdown import MarkItDown

# 定義 PDF 資料夾與目標 Markdown 資料夾路徑
pdf_folder = "PDF文件資料夾位置"
md_folder = "未來要儲存MD資料夾的位置"

# 確保目標 Markdown 資料夾存在
os.makedirs(md_folder, exist_ok=True)

# 初始化 MarkItDown
md = MarkItDown()

# 遍歷 PDF 資料夾內所有文件
for file_name in os.listdir(pdf_folder):
    if file_name.lower().endswith(".pdf"):  # 檢查是否為 PDF 文件
        pdf_path = os.path.join(pdf_folder, file_name)
        md_file_name = os.path.splitext(file_name)[0] + ".md"  # 將副檔名改為 .md
        md_path = os.path.join(md_folder, md_file_name)
        
        try:
            # 轉換 PDF 為 Markdown
            result = md.convert(pdf_path)
            markdown_content = result.text_content
            
            # 儲存 Markdown 文件
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            
            print(f"成功轉換並儲存：{md_path}")
        except Exception as e:
            print(f"轉換失敗：{pdf_path}，錯誤：{e}")
