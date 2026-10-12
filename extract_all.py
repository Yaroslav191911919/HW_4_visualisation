import fitz
import os

files = [
    (r"C:\Users\yar0s\Downloads\Неделя 1_Машинное обучение_Лонгрид_01546a3c (2).pdf", "week1.txt"),
    (r"C:\Users\yar0s\Downloads\Неделя 2_Машинное обучение_Лонгрид 1_0111522d (1).pdf", "week2_1.txt"),
    (r"C:\Users\yar0s\Downloads\Неделя 2_Машинное обучение_Лонгрид 2_01115305 (1).pdf", "week2_2.txt"),
    (r"C:\Users\yar0s\Downloads\Неделя 3-4_Машинное обучение_Лонгриد.pdf", "week3_4.txt"),
    (r"C:\Users\yar0s\Downloads\Неделя 5_Машинное обучение_Лонгрид.pdf", "week5.txt"),
]

output_dir = r"C:\Users\yar0s\OneDrive\Документы\Рабочий стол\hw viz"

for pdf_path, out_name in files:
    if os.path.exists(pdf_path):
        out_path = os.path.join(output_dir, out_name)
        doc = fitz.open(pdf_path)
        with open(out_path, "w", encoding="utf-8") as f:
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                f.write("--- Страница " + str(page_num + 1) + " ---\n")
                f.write(text)
                f.write("\n\n")
        doc.close()
        print("Извлечено: " + out_name)
    else:
        print("Файл не найден: " + pdf_path)
