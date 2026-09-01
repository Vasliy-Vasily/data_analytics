import os
import pandas as pd

def get_data():  # Get the data structure and the data itself from the user
    k = None
    c = None
    data = None
    number_of_groups = 0
    number_of_data = 0
    while True:
        c = float(input(
        "Выберите способ заполнения данных: 1) запись вручную\n"
        "2) загрузка файла\n"))
        if c == 1:
            while True:
                k = float(input(
                    "Выберите тип данных: 1) категориальные (конверсия, распределение по категориям: цвет кнопки, город, устройство и т.д.\n"
                    "2) количественные (средний чек, время, баллы, доход и т.д.)\n"))
                if k == 1:
                    print("Вы выбрали конверсию!")
                    while True:
                        number_of_groups = float(input("Введите количество групп (больше 1 и не больше 4)\n"))
                        if number_of_groups <= 4 and number_of_groups > 1 and number_of_groups.is_integer():
                            number_of_groups = int(number_of_groups)
                            break
                        print("Количество групп должно быть больше 1 и меньше или равно 4. Попробуйте снова")

                    while True:
                        number_of_data = float(input("Введите количество категорий данных (не меньше 2, не больше 10)\n"))
                        if number_of_data <= 10 and number_of_data > 1 and number_of_data.is_integer():
                            number_of_data = int(number_of_data)
                            break
                        print("Количество категорий данных должно быть больше 1 и меньше или равно 10. Попробуйте снова")
                    print("Приступаем к заполнению данных. Требования по заполнению данных:")
                    print(
                        "1) В каждый столбец записывайте непересекающиеся данные. Пример: столбцы (Купили; Всего пользователей) - неверно. Столбцы (Купили; Не купили) - верно. Программа сама посчитает общее количество.")
                    print(
                        "2) В случае данных о конверсии записывайте не доли, а количество для каждой категории данных.")
                    print("3) Не называйте столбец или строку 'Итого'\n")
                    columns = []

                    for i in range(number_of_data):
                        col_name = input(f"Введите название категории {i + 1}: ")
                        columns.append(col_name)
                    columns.append("Итого")
                    data = pd.DataFrame(columns=columns)

                    for i in range(number_of_groups):
                        group_name = input(f"Введите название группы номер {i + 1}: ")
                        val = []
                        for j in range(number_of_data):
                            val.append(float(input(f"Введите Значение{j + 1} для ({group_name}),({columns[j]}): ")))
                        val.append(0)
                        data.loc[group_name] = val

                    data["Итого"] = data.sum(axis=1)
                    data.loc["Итого"] = data.sum(axis=0)
                    data.loc["Итого", "Итого"] = 0
                    print("Ваши данные:")
                    print(data.to_string())
                    print('')
                    break
                elif k == 2:
                    print("Вы выбрали количественные данные или время!")
                    while True:
                        number_of_groups = float(input("Введите количество групп (больше 1 и не больше 4)\n"))
                        if number_of_groups <= 4 and number_of_groups > 1 and number_of_groups.is_integer():
                            number_of_groups = int(number_of_groups)
                            break
                        print("Количество групп должно быть больше 1 и меньше или равно 4. Попробуйте снова")
                    while True:
                        number_of_data = float(input("Введите количество данных (не меньше 2, не больше 100)\n"))
                        if number_of_data <= 100 and number_of_data > 1 and number_of_data.is_integer():
                            number_of_data = int(number_of_data)
                            break
                        print("Количество категорий данных должно быть больше 1 и меньше или равно 100. Попробуйте снова")
                    print("Приступаем к заполнению данных")
                    columns = []

                    for i in range(number_of_data):
                        columns.append(i + 1)
                    data = pd.DataFrame(columns=columns)

                    for i in range(number_of_groups):
                        group_name = input(f"Введите название группы номер {i + 1}: ")
                        val = []
                        for j in range(number_of_data):
                            val.append(float(input(f"Введите Значение{j + 1} для ({group_name}),({columns[j]}): ")))
                        data.loc[group_name] = val

                    print("Ваши данные")
                    print(data.to_string())
                    print('')
                    break
                else:
                    print("Выберите число 1 или 2")
            break
        elif c == 2:
            try:
                print("ВНИМАНИЕ!!! Файл должен называться data.csv")
                filename = "data.csv"
                if not os.path.exists(filename):
                    print(f"Ошибка: файл '{filename}' не найден!")
                    print("Убедитесь, что файл находится в той же папке, что и программа.")
                    continue
                data = pd.read_csv(filename)
                data = data.set_index(data.columns[0])
                number_of_groups = len(data)
                number_of_data = len(data.columns)
                while True:
                    k = float(input(
                        "Выберите тип данных: 1) категориальные (конверсия, распределение по категориям: цвет кнопки, город, устройство и т.д.\n"
                        "2) количественные (средний чек, время, баллы, доход и т.д.)\n"))
                    if k == 1:
                        print("Вы выбрали категориальные данные!")
                        data["Итого"] = data.sum(axis=1)
                        data.loc["Итого"] = data.sum(axis=0)
                        data.loc["Итого", "Итого"] = 0
                        break
                    elif k == 2:
                        print("Вы выбрали количественные данные!")
                        break
                    print("Выберите число 1 или 2")
                print("Ваши данные")
                print(data.to_string())
                print('')
                break
            except pd.errors.EmptyDataError:
                print("Ошибка: файл пуст!")
            except pd.errors.ParserError:
                print("Ошибка: неверный формат CSV файла!")
        else:
            print("Выберите число 1 или 2")


    return data, number_of_groups, number_of_data, k
