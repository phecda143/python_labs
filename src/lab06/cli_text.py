import argparse
from pathlib import Path
# from src.lib.moduls import text_stats
import sys

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent  # поднимаемся на два уровня вверх
sys.path.append(str(project_root))
# теперь импортируем относительно корня проекта
from src.lib.moduls import *


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    try:
        path_input = Path(args.input)
        sample = path_input.read_text(encoding='utf-8')

        if args.command == "cat":
            """ Реализация команды cat """
            for num, word in enumerate(sample.split('\n')):
                if args.n:
                    print(num + 1, word)
                else:
                    print(word)
        elif args.command == "stats":
            """ Реализация команды stats """
            print(
                f'Всего слов: {len(tokenize(normalize(sample)))}\nУникальных слов: {len(count_freq(tokenize(normalize(sample))))}')
            top_words = top_n(count_freq(tokenize(normalize(sample))))
            print("Топ-5:")
            for word, count in top_words:
                print(f"{word}: {count}")
    except FileNotFoundError:
        raise FileNotFoundError("Нет входного файла")


if __name__ == "__main__":
    main()
