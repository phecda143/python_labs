import re


def normalize(text, casefold=True, yo2e=True):
    if isinstance(text, str) and isinstance(casefold, bool) and isinstance(yo2e, bool):
        if casefold:
            text = text.casefold()
        if yo2e:
            text = text.replace("ё", "е")
            text = text.replace("Ё", "Е")
        if "\t" in text or "\n" in text or "\r" in text:
            text = text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    return " ".join(text.split())


def tokenize(text):
    if isinstance(text, str):
        text = re.sub(r"[^\w-]", " ", text).split()
    return text


def count_freq(tokens):
    if isinstance(tokens, list) and all(isinstance(item, str) for item in tokens):
        character_counting = dict()
        for i in sorted(set(tokens)):
            character_counting[i] = tokens.count(i)
    return character_counting


def top_n(freq, n=5):
    if isinstance(freq, dict) and all(
        isinstance(key, str) and isinstance(value, int) for key, value in freq.items()
    ):
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
