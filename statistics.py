from tests import z_test
from tests import xi_crit
from tests import welch_t_test
from tests import anova
from tests import kruskal_wallis
from tests import has_outliers
from tests import is_normal

#Define the statistical approach
def define_approach(df, number_of_groups, number_of_data, k, column=None, alternative=None):
    if k == 1:
        if number_of_groups == 2 and number_of_data == 2:
            print('Z-test is applied')
            print("p-value is:", z_test(df, number_of_groups, number_of_data, column, alternative))
            if z_test(df, number_of_groups, number_of_data, column, alternative) < 0.05:
                print("The difference is statistically significant. The null hypothesis is rejected.")
            else:
                print(
                    "The difference is not statistically significant. There is no reason to reject the null hypothesis.")
        else:
            print('Chi-square test is applied')
            user_value, table_value = xi_crit(df, number_of_groups, number_of_data)
            if user_value >= table_value:
                print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                      ", our value, which is ",
                      user_value, ", exceeds (or is equal to) the critical value", sep="")
                print("The difference is statistically significant. The null hypothesis is rejected.")
            else:
                print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                      ", our value, which is ", user_value, ", less than the critical value", sep="")
                print(
                    "The difference is not statistically significant. There is no reason to reject the null hypothesis.")
    elif k == 2:
        if number_of_groups == 2:
            if (not has_outliers(df, number_of_groups, number_of_data) and is_normal(df, number_of_groups, number_of_data)):
                print('The distribution is normal; there are no outliers')
                print('Welch t test test is applied')
                user_value, table_value = welch_t_test(df, number_of_groups, number_of_data)
                if user_value >= table_value:
                    print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                          ", our value, which is ",
                          user_value, ", exceeds (or is equal to) the critical value", sep="")
                    print("The difference is statistically significant. The null hypothesis is rejected.")
                else:
                    print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                          ", our value, which is ", user_value, ", less than the critical value", sep="")
                    print(
                        "The difference is not statistically significant. There is no reason to reject the null hypothesis.")
            else:
                print('The distribution is non-normal, or there are outliers')
                print('Kruskal-Wallis test is applied')
                user_value, table_value = kruskal_wallis(df, number_of_groups, number_of_data)
                if user_value >= table_value:
                    print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                          ", our value, which is ",
                          user_value, ", exceeds (or is equal to) the critical value", sep="")
                    print("The difference is statistically significant. The null hypothesis is rejected.")
                else:
                    print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                          ", our value, which is ", user_value, ", less than the critical value", sep="")
                    print(
                        "The difference is not statistically significant. There is no reason to reject the null hypothesis.")
        else:
            if (not has_outliers(df, number_of_groups, number_of_data) and is_normal(df, number_of_groups, number_of_data)):
                print('The distribution is normal; there are no outliers')
                print('ANOVA test is applied')
                user_value, table_value = anova(df, number_of_groups, number_of_data)
                if user_value >= table_value:
                    print("For the given number of degrees of freedom, the critical value is equal to ",
                          table_value,
                          ", our value, which is ",
                          user_value, ", exceeds (or is equal to) the critical value", sep="")
                    print("The difference is statistically significant. The null hypothesis is rejected.")
                else:
                    print("For the given number of degrees of freedom, the critical value is equal to ",
                          table_value,
                          ", our value, which is ", user_value, ", less than the critical value", sep="")
                    print(
                        "The difference is not statistically significant. There is no reason to reject the null hypothesis.")
            else:
                print('The distribution is non-normal, or there are outliers')
                print('Kruskal-Wallis test is applied')
                user_value, table_value = kruskal_wallis(df, number_of_groups, number_of_data)
                if user_value >= table_value:
                    print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                          ", our value, which is ",
                          user_value, ", exceeds (or is equal to) the critical value", sep="")
                    print("The difference is statistically significant. The null hypothesis is rejected.")
                else:
                    print("For the given number of degrees of freedom, the critical value is equal to ", table_value,
                          ", our value, which is ", user_value, ", less than the critical value", sep="")
                    print(
                        "The difference is not statistically significant. There is no reason to reject the null hypothesis.")
