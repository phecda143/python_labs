from pathlib import Path
import csv


def ensure_parent_dir(path: str | Path) -> None:
    """
    создать родительские директории, если их нет.
    аргументы:
        path: Путь к файлу или директории
    """
    path = Path(path)
    parent_dir = path.parent  # получение родительской директории
    parent_dir.mkdir(parents=True, exist_ok=True)  # создание директории


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """открыть тестовый файл и вернуть его содержимое как одну строку
    аргументы:
        path - путь к файлу
        encoding - кодировка файла (по умолчанию utf-8,
                    но если нужна другая можно указать, например: encoding="cp1251"
    возвращает:
        str: содержимое файла как одну строку
    Ошибки:
        UnicodeDecodeError: если содержимое не подходит под выбранную кодировку
        FileNotFoundError: файл не найден
    """
    ensure_parent_dir(path)  # создать родительскую директорию, если нужно
    try:
        with open(path, "r", encoding=encoding) as file:
            return " ".join(file.read().replace("\n", " ").split())
    except UnicodeDecodeError as e:
        raise ValueError(f"Неправильная кодировка") from e
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден") from e


# print(read_text('C:/Users/matve/PycharmProjects/python_labs/data/lab04/input.txt'))


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """Создать/перезаписать CSV с разделителем ,
    аргументы:
    rows - строки, которые надо записать(также надо проверить чтоб длина была одинакова)
        path - путь к файлу
        header - заголовок/1 строка, если задан то записать его первой строкой
    Ошибки:
        ValueError: не каждая строка в rows имеет одинаковую длину
    """
    p = Path(path)
    rows = list(rows)
    ensure_parent_dir(p)  # создать родительскую директорию, если нужно

    """'проверка, что все строки имеют одинаковую длину"""
    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(
                    f"Строка {i+1} имеет длину {len(row)}, ожидается {first_length}"
                )

    """проверка совпадения длины header с длиной строк"""
    if header is not None and rows:
        if len(header) != len(rows[0]):
            raise ValueError(
                f"Header имеет длину {len(header)}, а строки - {len(rows[0])}"
            )

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


# write_csv([("word","count"),("test",3)], "C:/Users/matve/PycharmProjects/python_labs/data/lab04/check.csv")
