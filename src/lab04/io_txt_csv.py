from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, 'r', encoding=encoding) as file:
        return ' '.join(file.read().replace("\n", ' ').split())