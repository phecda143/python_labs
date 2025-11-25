import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    """
    нормализация текста:
        приводит к нижнему регистру(если casefold=True)
        заменяет ё/Ё на е/Е(если yo2e=True)
        убирает невидимые управляющие символы
        схлопывает повторяющиеся пробелы в один
    """
    if isinstance(text, str) and isinstance(casefold, bool) and isinstance(yo2e, bool):
        if casefold:
            text = text.casefold()
        if yo2e:
            text = text.replace("ё", "е")
            text = text.replace("Ё", "Е")
        if "\t" in text or "\n" in text or "\r" in text:
            text = text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """
    токенизация:
        словом считается последовательность символов \w (буквы, цифры, подчёркивание)
        допускается дефис внутри слова
        числа также являются словами
        разделителями считаются все небуквенно-цифровые символы
    """
    if isinstance(text, str):
        text = re.sub(r"[^\w-]", " ", text).split()
        """ re.sub - функция замены в регулярках
            r'[^\w-] - все символы кроме \w (буквы/цифры/подчёркивание) и дефиса
        """
    return text


def count_freq(tokens: list[str]) -> dict[str, int]:
    """подсчитывает частоты, возвращает словарь"""
    if isinstance(tokens, list) and all(isinstance(item, str) for item in tokens):
        character_counting = dict()
        for i in sorted(set(tokens)):
            character_counting[i] = tokens.count(i)
    return character_counting


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ n по убыванию чамстоты; при равенстве - по алфавиту слова"""
    if isinstance(freq, dict) and all(
        isinstance(key, str) and isinstance(value, int) for key, value in freq.items()
    ):
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        """.items - возвращает ключ-значение
            key=lambda x сортировка по ключу lambda x, где x анонимная переменная
            -x[1] берет второй элемент(частоту слова) по убыванию
            x[0] берет первый элемент(само слово)
        """
    return sorted_items[:n]


print("normalize")
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print()
print("tokenize")
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print()
print("count_freq")
print(count_freq(["a", "b", "a", "c", "b", "a"]))
print(count_freq(["bb", "aa", "bb", "aa", "cc"]))
print()
print("top_n")
print(top_n({"a": 3, "b": 2, "c": 1}, n=2))
print(top_n({"aa": 2, "bb": 2, "cc": 1}, n=2))
