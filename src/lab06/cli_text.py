import argparse
from pathlib import Path
#from src.lib.moduls import text_stats
import sys
sys.path.append(str(Path(__file__).parent / 'lib'))
from moduls import text_stats

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
        sample = (path_input.read_text(encoding='utf-8')).split('\n')

        if args.command == "cat":
            """ Реализация команды cat """
            for num, word in enumerate(sample):
                if args.n:
                    print(num + 1, word)
                else:
                    print(word)
        elif args.command == "stats":
            """ Реализация команды stats """
            print(text_stats(sample))
    except FileNotFoundError:
        raise FileNotFoundError("Нет входного файла")


if __name__ == "__main__":
    main()
