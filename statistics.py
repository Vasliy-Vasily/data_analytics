from tests import z_test
from tests import xi_crit
from tests import welch_t_test
from tests import anova
from tests import kruskal_wallis
from tests import has_outliers
from tests import is_normal


def define_approach(df, number_of_groups, number_of_data, k):
    if k == 1:
        if number_of_groups == 2 and number_of_data == 2:
            z_test(df, number_of_groups, number_of_data)
        else:
            xi_crit(df, number_of_groups, number_of_data)

    elif k == 2:
        if number_of_groups == 2:
            if not has_outliers(df, number_of_groups, number_of_data) and is_normal(df, number_of_groups, number_of_data):
                welch_t_test(df, number_of_groups, number_of_data)
            else:
                kruskal_wallis(df, number_of_groups, number_of_data)

        else:
            if not has_outliers(df, number_of_groups, number_of_data) and is_normal(df, number_of_groups, number_of_data):
                anova(df, number_of_groups, number_of_data)
            else:
                kruskal_wallis(df, number_of_groups, number_of_data)