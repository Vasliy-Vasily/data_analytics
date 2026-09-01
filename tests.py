import math
import numpy as np

from critical_values import (
    z_table,
    xi_table,
    t_table,
    f_table,
    h_table,
)


# Checking for outliers
def has_outliers(df, number_of_groups, number_of_data):
    if number_of_data < 4:
        return False
    else:
        for i in range(number_of_groups):
            group_data = df.iloc[i,:]
            q1 = np.percentile(group_data, 25)
            q3 = np.percentile(group_data, 75)
            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            for value in group_data:
                if value < lower_bound or value > upper_bound:
                    return True
        return False


# Checking for normality of the distribution
def is_normal(df, number_of_groups, number_of_data):
    skew = 0
    s = 0
    kurt_sum = 0
    kurt = 0
    avg = 0
    if number_of_data < 3:
        return True
    else:
        for i in range(number_of_groups):
            sum = 0
            skew_sum = 0
            avg = df.iloc[i].sum() / number_of_data
            for j in range(number_of_data):
                sum += (df.iloc[i, j] - avg) ** 2
                skew_sum += (df.iloc[i, j] - avg) ** 3
            variance = sum / (number_of_data - 1)
            s = math.sqrt(variance)
            skew = skew_sum / (number_of_data * s ** 3)
            if skew <= -2 or skew >= 2:
                return False
            kurt_sum = 0
            for j in range(number_of_data):
                kurt_sum += (df.iloc[i, j] - avg) ** 4
            kurt = kurt_sum / (number_of_data * s ** 4) - 3
            if kurt >= 2 or kurt <= -2:
                return False
    return True


# Z-test
def z_test(df, number_of_groups, number_of_data):
    pooled = 0
    se = 0
    p_value = 0
    while True:
        number = float(input("Введите номер столбца с рассматриваемым показателем\n"))
        if number.is_integer() and (number == 1 or number == 2):
            number = int(number)
            break
        print("Такого столбца нет, введите заново")
    pooled = (df.iloc[0, number - 1] + df.iloc[1, number - 1]) / (df.iloc[0, -1] + df.iloc[1, -1])
    se = math.sqrt(pooled * (1 - pooled) * (1 / df.iloc[0, -1] + 1 / df.iloc[1, -1]))
    z = abs((df.iloc[0, number - 1] / df.iloc[0, -1] - df.iloc[1, number - 1] / df.iloc[1, -1]) / se)
    p_value = z_table(z)
    while True:
        hip = float(input("Выберите гипотезу: 1) односторонняя; 2) двусторонняя\n"))
        if hip == 1:
            print("p-value равно: ", p_value)
            if p_value < 0.05:
                print("Разница статистически значима. Нулевая гипотеза отвергнута.")
            else:
                print("Разница статистически не значима. Нет оснований отвергнуть нулевую гипотезу.")
            break
        elif hip == 2:
            d_p = p_value * 2
            print("p-value равно: ", d_p)
            if d_p < 0.05:
                print("Разница статистически значима. Нулевая гипотеза отвергнута.")
            else:
                print("Разница статистически не значима. Нет оснований отвергнуть нулевую гипотезу.")
            break
        print("Выберите число 1 или 2")


# Chi-square test
def xi_crit(df, number_of_groups, number_of_data):
    sum = 0
    degfr = 0
    exp_data = df.copy()
    del exp_data["Итого"]
    exp_data.drop(index="Итого", inplace=True)
    total = df["Итого"].sum()
    for i in range(number_of_groups):
        for j in range(number_of_data):
            exp_data.iloc[i, j] = (df.iloc[i, -1] * df.iloc[-1, j] / total)
    for i in range(number_of_groups):
        for j in range(number_of_data):
            sum += (df.iloc[i, j] - exp_data.iloc[i, j]) ** 2 / exp_data.iloc[i, j]
    degfr = (number_of_groups - 1) * (number_of_data - 1)
    sum = round (sum, 3)
    if sum >= xi_table(degfr):
        print("При данном количестве степеней свободы, критическое значение равно ", xi_table(degfr), ", наше значение, равное ",
              sum, ", превышает (или равно) критическое значение", sep="")
        print("Разница статистически значима. Нулевая гипотеза отвергнута.")
    else:
        print("При данном количестве степеней свободы, критическое значение равно ", xi_table(degfr),
              ", наше значение, равное ", sum, ", меньше критического значения", sep="")
        print("Разница статистически не значима. Нет оснований отвергнуть нулевую гипотезу.")


# T-test
def welch_t_test(df, number_of_groups, number_of_data):
    avg1 = 0
    avg2 = 0
    avg1 = df.iloc[0].sum() / number_of_data
    avg2 = df.iloc[1].sum() / number_of_data
    sum1 = 0
    sum2 = 0
    for i in range(number_of_data):
        sum1 += (df.iloc[0, i] - avg1) ** 2
        sum2 += (df.iloc[1, i] - avg2) ** 2
    dis1 = sum1 / (number_of_data - 1)
    dis2 = sum2 / (number_of_data - 1)
    se = math.sqrt(dis1 / number_of_data + dis2 / number_of_data)
    t = abs(avg1 - avg2) / se
    degfr = se ** 2 / ((dis1 / number_of_data) ** 2 / (number_of_data - 1) + (dis2 / number_of_data) ** 2 / (number_of_data - 1))

    if t >= t_table(degfr):
        print("При данном количестве степеней свободы, критическое значение равно ", t_table(degfr),
              ", наше значение, равное ",
              t, ", превышает (или равно) критическое значение", sep="")
        print("Разница статистически значима. Нулевая гипотеза отвергнута.")
    else:
        print("При данном количестве степеней свободы, критическое значение равно ", t_table(degfr),
              ", наше значение, равное ", t, ", меньше критического значения", sep="")
        print("Разница статистически не значима. Нет оснований отвергнуть нулевую гипотезу.")


# ANOVA method
def anova(df, number_of_groups, number_of_data):
    avg = []
    ssw = 0
    ssb = 0
    sst = 0
    msw = 0
    msb = 0
    f = 0
    for i in range(number_of_groups):
        sum = 0
        avg.append(df.iloc[i].sum() / number_of_data)
        for j in range(number_of_data):
            sum += (df.iloc[i, j] - avg[i]) ** 2
        ssw += sum
    gen_avg = sum(avg) / number_of_groups
    for i in range(number_of_groups):
        ssb += number_of_data * (avg[i] - gen_avg) ** 2
    sst = ssb + ssw
    msw = ssw / (number_of_groups * (number_of_data - 1))
    msb = ssb / (number_of_groups - 1)
    f = msb / msw
    degfr1 = number_of_groups - 1
    degfr2 = number_of_groups * (number_of_data - 1)
    if f >= f_table(degfr1, degfr2):
        print("При данном количестве степеней свободы, критическое значение равно ", f_table(degfr1, degfr2),
              ", наше значение, равное ",
              f, ", превышает (или равно) критическое значение", sep="")
        print("Разница статистически значима. Нулевая гипотеза отвергнута.")
    else:
        print("При данном количестве степеней свободы, критическое значение равно ", f_table(degfr1, degfr2),
              ", наше значение, равное ", f, ", меньше критического значения", sep="")
        print("Разница статистически не значима. Нет оснований отвергнуть нулевую гипотезу.")


# Kruskal-Wallis test
def kruskal_wallis(df, number_of_groups, number_of_data):
    rang = []
    for i in range(number_of_groups):
        for j in range(number_of_data):
            rang.append(df.iloc[i, j])
    sort = sorted(rang)
    rank_dict = {}
    i = 0
    freq = {}
    while i < len(sort):
        j = i
        while j < len(sort) and sort[j] == sort[i]:
            j += 1
        freq[sort[i]] = j - i
        rank = (i + j + 1) / 2
        rank_dict[sort[i]] = rank
        i = j
    rang_list = []
    for i in range(len(rang)):
        rang_list.append(rank_dict[rang[i]])
    R = [0] * number_of_groups
    idx = 0
    for i in range(number_of_groups):
        for j in range(number_of_data):
            R[i] += rang_list[idx]
            idx += 1
    h_corr = 0
    N = number_of_groups * number_of_data
    h = 0
    l = 0
    for i in range(number_of_groups):
        l += (R[i] ** 2) / number_of_data
    h = (12 / (N * (N + 1))) * l - 3 * (N + 1)
    k_sum = 0
    for value in freq.values():
        k_sum += value ** 3 - value
    h_corr = h / (1 - k_sum / ((number_of_groups * number_of_data) ** 3 - (number_of_groups * number_of_data)))
    degfr = number_of_groups - 1
    if h_corr >= h_table(degfr):
        print("При данном количестве степеней свободы, критическое значение равно ", h_table(degfr),
              ", наше значение, равное ",
              h_corr, ", превышает (или равно) критическое значение", sep="")
        print("Разница статистически значима. Нулевая гипотеза отвергнута.")
    else:
        print("При данном количестве степеней свободы, критическое значение равно ", h_table(degfr),
              ", наше значение, равное ", h_corr, ", меньше критического значения", sep="")
        print("Разница статистически не значима. Нет оснований отвергнуть нулевую гипотезу.")
