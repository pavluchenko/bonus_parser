
import openpyxl

def parse_and_save_to_excel(input_file, output_file):
    # Чтение данных из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        data = [line.split() for line in file.readlines()]

    # Создание нового файла Excel и заполнение данными
    wb = openpyxl.Workbook()
    ws = wb.active

    for row_index, row_data in enumerate(data, start=1):
        for col_index, cell_data in enumerate(row_data, start=1):
            ws.cell(row=row_index, column=col_index, value=cell_data)

    # Сохранение файла Excel
    wb.save(output_file)

if __name__ == "__main__":
    input_file_path = '...\\update_bonuses.txt'  # Путь к вашему текстовому файлу
    output_file_path = '...\\update_bonuses_table.xlsx'  # Путь, по которому будет сохранен файл Excel

    parse_and_save_to_excel(input_file_path, output_file_path)
