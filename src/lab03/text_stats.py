import sys
'''добавляем нужный нам путь в список путей, где Python ищет модули при импорте'''
sys.path.append('C:/Users/matve/PycharmProjects/python_labs/src/lib')
'''импортируем созданные ранее функции'''
from src.lib.moduls import normalize, tokenize, count_freq, top_n
data = sys.stdin.read()
data = [i.casefold() for i in tokenize(normalize(data))]
print(f'Всего слов: {len(data)}\nУникальных слов: {len(set(data))}')
f=False
if f:
    longest_word = len(max(count_freq(data), key=len))+5
    print(f'слово{(longest_word-5) * " "}| частота')
    print((longest_word + 9) * '-')
    print('\n'.join([word[0] + ' ' * (longest_word-len(word[0])) + '| ' + str(word[1]) for word in top_n(count_freq(data))]))
else:
    top_words = top_n(count_freq(data))
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}: {count}")

#hello world hello python test world hello