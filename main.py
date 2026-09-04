import argparse

from data_input import get_data
from statistics import define_approach
from unit_tests import unit_test_result


def parse_arguments():
    parser = argparse.ArgumentParser(description="Statistical analysis of an A/B test")
    parser.add_argument("--file", type=str, required=True, help="Path to the CSV file")
    parser.add_argument("--type", choices=["categorical", "quantitative"], required=True, help="Data type")
    parser.add_argument("--column", type=int, choices=[1, 2], help="Data category number for the Z-test" )
    parser.add_argument("--alternative", choices=["one-sided", "two-sided"], help="Hypothesis type for the Z-test" )
    parser.add_argument("--unit-test", action="store_true", help="Run unit tests"  )
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.unit_test:
        if not unit_test_result():
            print("Program cannot run because there are errors.")
            return
    print("STATISTICAL ANALYSIS OF AN A/B TEST")
    print()
    df, number_of_groups, number_of_data, k = get_data(args)
    define_approach(df, number_of_groups, number_of_data, k, args.column, args.alternative)

if __name__ == "__main__":
    main()
