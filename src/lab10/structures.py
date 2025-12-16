from collections import deque


class Stack:
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        # обработка случая пустого стека (сейчас IndexError от list)
        if self.is_empty():
            raise IndexError('Пустой стек')
        return self._data.pop()

    def peek(self):
        # Вернуть верхний элемент без удаления.
        # ошибка: при пустом стеке будет None
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        # Проверить, пуст ли стек
        # возвратить: True если стек пуст, иначе False
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class Queue:
    '''Структура данных "Очередь" (FIFO - First In, First Out)
        Реализация на базе collections.deque'''

    def __init__(self):
        # Инициализация пустой очереди
        self._data = deque()

    def enqueue(self, item):
        # Добавить элемент в конец очереди.
        self._data.append(item)

    def dequeue(self):
        # Взять элемент из начала очереди и вернуть его.
        # Если очередь пустая - IndexError
        if self.is_empty():
            raise IndexError('Пустая очередь')
        return self._data.popleft()

    def peek(self):
        # Вернуть первый элемент без удаления.
        if not self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        # Проверить, пуста ли очередь.
        return len(self._data) == 0

    def __len__(self):
        # количество элементов в очереди
        return len(self._data)


print('===Stack===')
stack = Stack()
print(f'Пустой стек: {stack.is_empty()}')  # True
# добавляем элементы
stack.push(10)
stack.push(20)
stack.push(30)
print(f'размер стека после добавления 3 элементов: {len(stack)}')  # 3
# верхний элемент без удаления
print(f'верхний элемент (peek): {stack.peek()}')  # 30
# удаляем элементы (LIFO - Last In First Out)
print(f'удаляем {stack.pop()}')  # 30
print(f'удаляем {stack.pop()}')  # 20
print(f'оставшийся размер: {len(stack)}')  # 1
# удаляем все
while not stack.is_empty():
    print(f'удаляем: {stack.pop()}')
print(f'cтек пустой: {stack.is_empty()}')  # True
print(f'peek из пустого стека: {stack.peek()}')  # None
# пример с ошибкой при pop из пустого стека
try:
    stack.pop()
except IndexError as e:
    print(f'ошибка при удалении из пустого стека: {e}')


# пример использования Queue
print('===Queue===')
queue = Queue()
print(f'пустая очередь: {queue.is_empty()}')  # True
# добавляем элементы
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'размер очереди после добавления 3 элементов: {len(queue)}')  # 3
# первый элемент без удаления
print(f'первый элемент: {queue.peek()}') # 1
# удаляем элементы (FIFO - First In First Out)
print(f'удаляем (dequeue): {queue.dequeue()}')  # 1
print(f'удаляем (dequeue): {queue.dequeue()}')  # 2
print(f'оставшийся размер: {len(queue)}')  # 1
# удаляем всё
while not queue.is_empty():
    print(f'удаляем {queue.dequeue()}')
print(f'очередь пустая: {queue.is_empty()}')  # True
# пример с ошибкой при dequeue из пустой очереди
try:
    queue.dequeue()
except IndexError as e:
    print(f'ошибка при dequeue из пустой очереди: {e}')  # Пустая очередь