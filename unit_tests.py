import pandas as pd
from tests import z_test
from tests import xi_crit
from tests import welch_t_test
from tests import anova
from tests import kruskal_wallis
from tests import has_outliers
from tests import is_normal

# Here we gonna check all the tests. We create test DataFrames and verify the correctness of each method's operation using this DataFrame
data_for_unit_test_z = pd.DataFrame({
    'Bought': [500, 550, 1050],
    'Did not buy': [9500, 9450, 18950],
    'Total': [10000, 10000, 0]
}, index=['A', 'B', 'Total'])

def unit_test_z():
    if(z_test(data_for_unit_test_z, 2, 2, 1, "one-sided")) != 0.056:
        return False
    else:
        return True

data_for_unit_test_xi_crit = pd.DataFrame({
    'Blue': [500, 550, 400, 1450],
    'Red': [550, 450, 500, 1500],
    'Green': [600, 550, 600, 1750],
    'Total': [1650, 1550, 1500, 0]
}, index=['A', 'B', 'C', 'Total'])

def unit_test_xi_crit():
    check_user, check_table = xi_crit(data_for_unit_test_xi_crit, 3, 3)
    if check_user != 30.171 or check_table != 9.488:
        return False
    else:
        return True

data_for_unit_test_welch_t = pd.DataFrame({
    1: [11, 18],
    2: [12, 19],
    3: [13, 20],
    4: [10, 21],
    5: [14, 20]
}, index=['A', 'B'])

def unit_test_welch_t():
    check_user, check_table = welch_t_test(data_for_unit_test_welch_t, 2, 5)
    if check_user != 8.718 or check_table != 2.228:
        return False
    else:
        return True

data_for_unit_test_kruskal_wallis = pd.DataFrame({
    1: [11, 18, 28],
    2: [12, 19, 23],
    3: [13, 20, 25],
    4: [50, 21, 19],
    5: [14, 20, 21]
}, index=['A', 'B', 'C'])

def unit_test_kruskal_wallis():
    check_user, check_table = kruskal_wallis(data_for_unit_test_kruskal_wallis, 3, 5)
    if check_user != 4.846 or check_table != 5.991:
        return False
    else:
        return True

data_for_unit_test_anova = pd.DataFrame({
    1: [11, 18, 28],
    2: [12, 19, 23],
    3: [13, 20, 25],
    4: [10, 21, 19],
    5: [14, 20, 21]
}, index=['A', 'B', 'C'])

def unit_test_anova():
    check_user, check_table = anova(data_for_unit_test_anova, 3, 5)
    if check_user != 30.65 or check_table != 3.89:
        return False
    else:
        return True

data_for_unit_test_is_normal_1 = pd.DataFrame({
    1: [102, 98, 101],
    2: [107, 103, 106],
    3: [112, 108, 111],
    4: [105, 101, 104],
    5: [108, 104, 107],
    6: [103, 99, 102],
    7: [109, 105, 108],
    8: [106, 102, 105],
    9: [104, 100, 103],
    10: [110, 106, 109]
}, index=['A', 'B', 'C'])
data_for_unit_test_is_normal_2 = pd.DataFrame({
    1: [103, 99, 5],
    2: [85, 90, 82],
    3: [93, 89, 200],
    4: [95, 150, 88],
    5: [88, 85, 95],
    6: [92, 88, 90],
    7: [90, 91, 85],
    8: [87, 86, 91],
    9: [94, 93, 10],
    10: [91, 87, 94]
}, index=['A', 'B', 'C'])

def unit_test_is_normal():
    if is_normal(data_for_unit_test_is_normal_1, 3, 10) == True and is_normal(data_for_unit_test_is_normal_2, 3, 10) == False:
        return True
    else:
        return False

data_for_unit_test_has_outliers_1 = pd.DataFrame({
    1: [102, 98, 101],
    2: [107, 103, 106],
    3: [112, 108, 111],
    4: [105, 101, 104],
    5: [108, 104, 107],
    6: [103, 99, 102],
    7: [109, 105, 108],
    8: [106, 102, 105],
    9: [104, 100, 103],
    10: [110, 106, 109]
}, index=['A', 'B', 'C'])
data_for_unit_test_has_outliers_2 = pd.DataFrame({
    1: [102, 98, 101],
    2: [107, 103, 106],
    3: [112, 108, 111],
    4: [105, 101, 104],
    5: [108, 104, 107],
    6: [103, 99, 102],
    7: [109, 105, 108],
    8: [106, 102, 105],
    9: [104, 1000, 103],
    10: [110, 106, 109]
}, index=['A', 'B', 'C'])

def unit_test_has_outliers():
    if has_outliers(data_for_unit_test_has_outliers_1, 3, 10) == False and has_outliers(data_for_unit_test_has_outliers_2, 3, 10) == True:
        return True
    else:
        return False

def unit_test_result():
    if unit_test_z() == False:
        print("Z-test code has an error")
    if unit_test_xi_crit() == False:
        print("Chi-square test code has an error")
    if unit_test_welch_t() == False:
        print("Welch t test code has an error")
    if unit_test_kruskal_wallis() == False:
        print("Kruskal_Wallis test code has an error")
    if unit_test_anova() == False:
        print("ANOVA test code has an error")
    if unit_test_is_normal() == False:
        print("Function for testing the normality of a distribution code has an error")
    if unit_test_has_outliers() == False:
        print("Outlier detection function code has an error")
    if unit_test_z() == True and unit_test_xi_crit() == True and unit_test_welch_t() == True and unit_test_kruskal_wallis() == True and unit_test_anova() == True and unit_test_is_normal() == True and unit_test_has_outliers() == True:
        print('Unit testes have been done. All tests work correctly.')
        return True
    else:
        return False
