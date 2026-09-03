import argparse

from data_input import get_data
from statistics import define_approach
from unit_tests import unit_test_result


def parse_arguments(): #Command line processing
    parser = argparse.ArgumentParser(
        description="Statistical analysis of an A/B test"
    )
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the CSV file"
    )
    parser.add_argument(
        "--type",
        choices=["categorical", "quantitative"],
        required=True,
        help="Data type"
    )
    parser.add_argument(
        "--column",
        type=int,
        choices=[1, 2],
        help="Data category number for the Z-test"
    )
    parser.add_argument(
        "--alternative",
        choices=["one-sided", "two-sided"],
        help="Hypothesis type for the Z-test"
    )
    return parser.parse_args()


def main():
    if unit_test_result() == False:
        print('Programm can not run with errors')
    else:
        print("STATISTICAL ANALYSIS OF AN A/B TEST")
        print()
        args = parse_arguments()
        df, number_of_groups, number_of_data, k = get_data(args)
        define_approach(df, number_of_groups, number_of_data, k, args.column, args.alternative)


if __name__ == "__main__":
    main()
