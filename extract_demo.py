import fitz
import os

file_path = r"C:\Users\yar0s\Downloads\Коллоквиум 1 — Демо-вариант.pdf"

if os.path.exists(file_path):
    doc = fitz.open(file_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        print("--- Страница " + str(page_num + 1) + " ---")
        print(text)
    doc.close()
else:
    print("Файл не найден: " + file_path)
