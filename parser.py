import re

def process_file(input_file_path, output_file_path, regex_pattern):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            input_content = input_file.read()
        processed_content = re.sub(regex_pattern, '', input_content)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_content)

        print(f"Программа успешно выполнена. Результат записан в {output_file_path}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
input_file_path = "...\\bonuses.rb"
output_file_path = "...\\update_bonuses.txt"
regex_pattern = r'on :|,| 1 do|4|>1| 2 do|do|end'

process_file(input_file_path, output_file_path, regex_pattern)
