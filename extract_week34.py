import fitz
import os

file_path = r"C:\Users\yar0s\Downloads\Неделя 3-4_Машинное обучение_Лонгрид.pdf"
out_path = r"C:\Users\yar0s\OneDrive\Документы\Рабочий стол\hw viz\week3_4.txt"

if os.path.exists(file_path):
    doc = fitz.open(file_path)
    with open(out_path, "w", encoding="utf-8") as f:
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            f.write("--- Страница " + str(page_num + 1) + " ---\n")
            f.write(text)
            f.write("\n\n")
    doc.close()
    print("Извлечено: week3_4.txt")
else:
    print("Файл не найден: " + file_path)
