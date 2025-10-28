import sys
import os
from pathlib import Path

current_dir = Path(__file__).parent
'''__file__ - полный путь файла
    Path(__file__) - создание объекта path из этого пути
    .parent - родительская директория'''
project_root = current_dir.parent.parent  # поднимаемся на два уровня вверх
sys.path.append(str(project_root / 'src' / 'lib'))

from src.lib.moduls import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def console_output(text): # вывод в консоль из файла input.txt
    all_tokens = tokenize(normalize(text))
    top_words = top_n(count_freq(all_tokens))
    output = f"Всего слов: {len(all_tokens)}"
    output += f"\nУникальных слов: {len(set(all_tokens))}"
    output += "\nТоп-5:"
    for word, count in top_words:
        output += f"\n{word}:{count}"
    return output


def from_file_to_text(path, encoding='utf-8'): # перевод содержимое файла input.txt в единую строку
    return read_text(path, encoding=encoding)


def frequencies_from_text(text: str) -> dict[str, int]: # токенизация, нормализация, счет частоты слов из ЛР3
    tokens = top_n(count_freq(tokenize(normalize(text))))
    return tokens


def text_to_csv(rows, path=str(project_root / 'data' / 'lab04' / 'report.csv'), header=("word", "count")):
    # запись в scv
    # если файл input.txt - пустой, то в файле report.csv только заголовок
    return write_csv(rows, path=path, header=header)


text_content = from_file_to_text(str(project_root / 'data' / 'lab04' / 'input.txt'))
text_to_csv(frequencies_from_text(text_content))
print(console_output(text_content))
