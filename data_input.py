import os
import pandas as pd


def get_data(args): #Get data from the user
    filename = args.file

    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"Файл '{filename}' не найден."
        )

    try:
        data = pd.read_csv(filename)
    except pd.errors.EmptyDataError:
        raise ValueError("CSV-файл пуст.")
    except pd.errors.ParserError:
        raise ValueError("Неверный формат CSV-файла.")

    data = data.set_index(data.columns[0])

    number_of_groups = len(data)
    number_of_data = len(data.columns)

    if args.type == "categorical":
        k = 1

        data["Итого"] = data.sum(axis=1)
        data.loc["Итого"] = data.sum(axis=0)
        data.loc["Итого", "Итого"] = 0

    else:
        k = 2

    print("\nВаши данные:")
    print(data.to_string())
    print()

    return data, number_of_groups, number_of_data, k
