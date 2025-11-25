import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    if not (json_path.endswith(".json")) or not (csv_path.endswith(".csv")):
        raise TypeError("Неправильный формат файла")
    try:
        with open(json_path, "r", encoding="utf-8") as jf:
            file = json.load(jf)  # возвращает список словарей
        if not isinstance(file, list):
            raise ValueError("JSON должен содержать список объектов")
        if len(file) == 0:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        if not isinstance(file[0], dict):
            raise ValueError("Элементы списка должны быть словарями")

        with open(csv_path, "w", encoding="utf-8") as cf:
            cf = csv.DictWriter(cf, fieldnames=list(file[0].keys()))
            cf.writeheader()
            cf.writerows(file)

    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    if not (json_path.endswith(".json")) or not (csv_path.endswith(".csv")):
        raise TypeError("Неправильный формат файла")
    try:
        with open(csv_path, "r", encoding="utf-8") as cf:
            file = list(csv.DictReader(cf))
        if len(file) == 0:
            raise ValueError("CSV файл пуст")

        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(file, jf, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
