import argparse
from pathlib import Path
import sys

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent  # поднимаемся на два уровня вверх
sys.path.append(str(project_root))
# теперь импортируем относительно корня проекта
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv':
            json_to_csv(args.input, args.output)
        if args.cmd == 'csv2json':
            csv_to_json(args.input, args.output)
        if args.cmd == 'csv2xlsx':
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        raise FileNotFoundError('Нет входного файла')


if __name__ == "__main__":
    main()
