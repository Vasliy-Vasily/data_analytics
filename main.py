import argparse

from data_input import get_data
from statistics import define_approach


def parse_arguments(): #Command line processing
    parser = argparse.ArgumentParser(
        description="Статистический анализ A/B теста"
    )

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Путь к CSV-файлу"
    )

    parser.add_argument(
        "--type",
        choices=["categorical", "quantitative"],
        required=True,
        help="Тип данных"
    )

    return parser.parse_args()


def main():
    print("СТАТИСТИЧЕСКИЙ АНАЛИЗ A/B ТЕСТА\n")

    args = parse_arguments()

    df, number_of_groups, number_of_data, k = get_data(args)

    define_approach(
        df,
        number_of_groups,
        number_of_data,
        k
    )


if __name__ == "__main__":
    main()
