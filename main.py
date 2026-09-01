from data_input import get_data
from statistics import define_approach


def main():
    print("СТАТИСТИЧЕСКИЙ АНАЛИЗ A/B ТЕСТА")
    print(
        "ВВЕДИТЕ ДАННЫЕ И ИХ ХАРАКТЕРИСТИКИ, "
        "А ПРОГРАММА ОПРЕДЕЛИТ ВЕРНЫЙ "
        "СТАТИСТИЧЕСКИЙ ПОДХОД И ПРИМЕНИТ ЕГО"
    )

    df, number_of_groups, number_of_data, k = get_data()
    define_approach(df, number_of_groups, number_of_data, k)


if __name__ == "__main__":
    main()