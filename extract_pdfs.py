import fitz
import os

files = [
    r"C:\Users\yar0s\Downloads\Коллоквиум 1 — Демо-вариант.pdf",
    r"C:\Users\yar0s\Downloads\Неделя 1_Машинное обучение_Лонгрид_01546a3c (2).pdf",
    r"C:\Users\yar0s\Downloads\Неделя 2_Машинное обучение_Лонгрид 1_0111522d (1).pdf",
    r"C:\Users\yar0s\Downloads\Неделя 2_Машинное обучение_Лонгрид 2_01115305 (1).pdf",
    r"C:\Users\yar0s\Downloads\Неделя 3-4_Машинное обучение_Лонгрид.pdf",
    r"C:\Users\yar0s\Downloads\Неделя 5_Машинное обучение_Лонгрид.pdf"
]

for file_path in files:
    if os.path.exists(file_path):
        print("=" * 80)
        print("ФАЙЛ: " + os.path.basename(file_path))
        print("=" * 80)
        doc = fitz.open(file_path)
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            print("\n--- Страница " + str(page_num + 1) + " ---")
            print(text)
        doc.close()
    else:
        print("Файл не найден: " + file_path)
