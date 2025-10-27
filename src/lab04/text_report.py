import sys
'''добавляем нужный нам путь в список путей, где Python ищет модули при импорте'''
sys.path.append('C:/Users/matve/PycharmProjects/python_labs/src/lib')
'''импортируем созданные ранее функции'''
from src.lib.moduls import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv

def console_output(text): # вывод в консоль из файла input.txt
    tokens = top_n(count_freq(tokenize(normalize(text))))
    return f'Всего слов: {len(tokens)}\nУникальных слов: {len(set(tokens))}\nТоп-5:\n{'\n'.join((f'{i[0]}:{i[1]}' for i in tokens))}'

def from_file_to_text(path, encoding='utf-8'): # перевод содержимое файла input.txt в единую строку
    return read_text(path, encoding=encoding)

def frequencies_from_text(text: str) -> dict[str, int]: # токенизация, нормализация, счет частоты слов из ЛР3
    tokens = top_n(count_freq(tokenize(normalize(text))))
    return tokens

def text_to_csv(rows, path='C:/Users/matve/PycharmProjects/python_labs/data/lab04/report.csv', header=("word", "count")):
    # запись в scv
    # если файл input.txt - пустой, то в файле report.csv только заголовок
    return write_csv(rows, path=path, header=header)

text_to_csv(frequencies_from_text(from_file_to_text('C:/Users/matve/PycharmProjects/python_labs/data/lab04/input.txt')))
print(console_output(from_file_to_text('C:/Users/matve/PycharmProjects/python_labs/data/lab04/input.txt')))



