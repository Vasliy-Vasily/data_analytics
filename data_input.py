import os
import pandas as pd


def get_data(args): #Get data from the user
    filename = args.file
    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"File '{filename}' is not found!"
        )
    try:
        data = pd.read_csv(filename)
    except pd.errors.EmptyDataError:
        raise ValueError("Error: file is empty!")
    except pd.errors.ParserError:
        raise ValueError("Error: invalid format for CVS file!")
    data = data.set_index(data.columns[0])
    number_of_groups = len(data)
    number_of_data = len(data.columns)
    if args.type == "categorical":
        k = 1
        data = data.apply(pd.to_numeric)
        data["Total"] = data.sum(axis=1)
        data.loc["Total"] = data.sum(axis=0)
        data.loc["Total", "Total"] = 0
    else:
        k = 2
        data = data.apply(pd.to_numeric)
    print("Your data:")
    print(data.to_string())
    print()
    return data, number_of_groups, number_of_data, k
