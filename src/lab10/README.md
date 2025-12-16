# ЛР10 — Структуры данных: Stack, Queue, Linked List и бенчмарки

> **Цель:** реализовать базовые структуры данных (стек, очередь, связный список),
> сравнить их производительность и научиться думать в терминах асимптотики (O(1), O(n)). 

### Стек (Stack)

**Стек** — это структура данных, работающая по принципу "последним пришёл — первым вышел" (LIFO, Last In First Out). 
Представляет собой список элементов, организованных по принципу LIFO.

**Основные операции:**
- `push(item)` — добавить элемент на вершину стека — **O(1)**
- `pop()` — извлечь верхний элемент — **O(1)**
- `peek()` — посмотреть верхний элемент без извлечения — **O(1)**
- `is_empty()` — проверить, пуст ли стек — **O(1)**

**Применение:**
- Обратная польская нотация
- Рекурсивные вызовы функций
- Отмена операций (undo)

### Очередь (Queue)

**Очередь** — это структура данных, работающая по принципу "первым пришёл — первым вышел" (FIFO, First In First Out).
Представляет собой список элементов, организованных по принципу FIFO.

**Основные операции:**
- `enqueue(item)` — добавить элемент в конец очереди — **O(1)**
- `dequeue()` — извлечь первый элемент — **O(1)**
- `peek()` — посмотреть первый элемент без извлечения — **O(1)**
- `is_empty()` — проверить, пуста ли очередь — **O(1)**

**Применение:**
- Планирование задач
- Обработка запросов
- Алгоритмы обхода графов

### Связный список (Linked List)

**Связный список** — это структура данных, состоящая из узлов, каждый из которых содержит данные и ссылку (указатель) на следующий узел в последовательности.

**Односвязный список (Singly Linked List):**
- Каждый узел содержит данные и указатель на следующий узел
- Первый узел называется "головой" (head)
- Последний узел указывает на `None`

**Основные операции:**
- `append(value)` — добавить элемент в конец — **O(1)** (при наличии tail)
- `prepend(value)` — добавить элемент в начало — **O(1)**
- `insert(idx, value)` — вставить элемент по индексу — **O(n)**
- `remove(value)` — удалить элемент по значению — **O(n)**
- `remove_at(idx)` — удалить элемент по индексу — **O(n)**

**Преимущества:**
- Динамический размер
- Эффективная вставка и удаление в начале — **O(1)**

**Недостатки:**
- Доступ к элементу по индексу — **O(n)**
- Дополнительная память на хранение указателей

---

## Реализация

### Задание A. Реализовать Stack и Queue (src/lab10/structures.py)
```python
from collections import deque


class Stack:
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        # TODO: добавить обработку случая пустого стека (сейчас IndexError от list)
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
```

<img src="https://github.com/phecda143/python_labs/blob/8703d2a77856a29cc4156442d50fa22dde938961/images/lab10/structures1.png" alt="Картинка 10.1" />
<img src="https://github.com/phecda143/python_labs/blob/8703d2a77856a29cc4156442d50fa22dde938961/images/lab10/structures2.png" alt="Картинка 10.2" />

```
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
```

```
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
```

### B. Реализовать SinglyLinkedList (src/lab10/linked_list.py)
```python
class Node:  # узел односвязного списка.
    def __init__(self, value, next=None):
        self.value = value  # значение элемента.
        self.next = next  # ссылка на следующий узел или None, если это последний узел.


class SinglyLinkedList:  # односвязный список, состоящий из узлов Node
    def __init__(self):
        self.head: Node | None = None  # первый узел
        self.tail: Node | None = None  # хвост списка (последний элемент) для ускорения append
        # ошибка: размер не обновляется
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            # если список пуст, новый узел становится и head и tail
            self.head = new_node
            self.tail = new_node
        else:
            # добавляем после tail и обновляем tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:  # оптимизация для вставки в конец
            self.append(value)
            return

        current = self.head
        # Нет ошибки: idx проверен выше, current гарантированно не None для idx > 0
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node

        # обновляем tail если вставили после него
        if current == self.tail:
            self.tail = new_node

        self._size += 1  # увеличиваем размер

    def remove(self, value):
        """Удалить первое вхождение значения value"""
        if self.head is None:
            return  # список пуст, нечего удалять

        # eсли удаляем первый элемент
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:  # если список стал пустым
                self.tail = None
            return

        # ищем элемент для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        # если нашли элемент для удаления
        if current.next is not None:
            current.next = current.next.next
            self._size -= 1
            # если удалили последний элемент
            if current.next is None:
                self.tail = current

    def remove_at(self, idx):
        """удалить элемент по индексу idx"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size - 1}]")

        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:  # если список стал пустым
                self.tail = None
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        # удаляем элемент
        current.next = current.next.next
        self._size -= 1

        # обновляем tail если удалили последний элемент
        if current.next is None:
            self.tail = current

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

```

```
lst = SinglyLinkedList()
# добавление элементов
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)  # SinglyLinkedList([1, 2, 3])
print(len(lst))  # 3
# добавление в начало
lst.prepend(0)
print(lst)  # SinglyLinkedList([0, 1, 2, 3])
# вставка по индексу
lst.insert(2, 99)
print(lst)  # SinglyLinkedList([0, 1, 99, 2, 3])
# вставка в конец
lst.insert(5, 100)
print(lst)  # SinglyLinkedList([0, 1, 99, 2, 3, 100])
# удаление по значению
lst.remove(99)
print(lst)  # SinglyLinkedList([0, 1, 2, 3, 100])
# удаление по индексу
lst.remove_at(0)
print(lst)  # SinglyLinkedList([1, 2, 3, 100])
# проверка граничных случаев
print(len(lst))  # 4
print(lst.tail.value if lst.tail else None)  # 100
```

<img src="https://github.com/phecda143/python_labs/blob/8703d2a77856a29cc4156442d50fa22dde938961/images/lab10/linked_list.png" alt="Картинка 10.3" />


### Выводы по бенчмаркам

Стек — самая быстрая структура данных:
 - Реализация на базе списка Python (list)
 - append() и pop() работают за амортизированное O(1)
 - Минимальные накладные расходы

Очередь — немного медленнее стека:
 - Использует deque из collections
 - append() и popleft() работают за O(1)
 - Все ещё значительно быстрее связных списков

Односвязный список — самая медленная из трёх:
 - Каждая операция требует создания объекта Node
 - Нет локальности данных (разрозненное хранение в памяти)
 - Много операций с указателями
 - Для удаления элемента по индексу требуется O(n) операций

Рекомендации по выбору структуры данных:
 - Используйте стек когда: нужен LIFO доступ, требуется максимальная производительность
 - Используйте очередь когда: нужен FIFO доступ, обрабатываете задачи по порядку
 - Используйте связный список когда: частые вставки/удаления в середине, производительность не критична