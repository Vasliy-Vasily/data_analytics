from data_input import get_data
from statistics import define_approach


def main():
    print("STATISTICS ANALISYS OF A/B TEST")
    print(
        "ENTER THE DATA AND ITS CHARACTERISTICS, "
        "AND THE PROGRAM WILL DEFINE THE CORRECT "
        "STATISTICAL APPROACH AND WILL APPLY IT"
    )

    df, number_of_groups, number_of_data, k = get_data()
    define_approach(df, number_of_groups, number_of_data, k)


if __name__ == "__main__":
    main()
