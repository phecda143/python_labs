import sys
from src.lib.moduls import count_freq,  top_n, tokenize
data = sys.stdin.read()
data = [i.casefold() for i in tokenize(data)]
print(f'Всего слов: {len(data)}\nУникальных слов: {len(set(data))}')
f=False
if f:
    longest_word = len(max(count_freq(data), key=len))+5
    print(f'слово{(longest_word-5) * ' '}| частота')
    print((longest_word + 9) * '-')
    print('\n'.join([word[0] + ' ' * (longest_word-len(word[0])) + '| ' + str(word[1]) for word in top_n(count_freq(data))]))
else:
    print(f'Топ-5:\n{'\n'.join((f'{i[0]}:{i[1]}' for i in top_n(count_freq(data))))}')