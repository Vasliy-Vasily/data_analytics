# Statistical Analysis of an A/B Test

A command-line Python application for statistical analysis of A/B test results.
The program accepts data from a CSV file, determines an appropriate statistical test based on the data type and experiment structure, performs the required calculations, 
and reports whether the observed difference is statistically significant.
This project was created for educational purposes to practice Python, statistical analysis, Pandas, hypothesis testing, and modular software design.

---

# Features

- Load data from CSV files
- Support for categorical and quantitative data
- Automatic selection of a statistical method
- Z-test for conversion comparison
- Chi-square (χ²) test for categorical data
- Welch's t-test for quantitative data
- ANOVA for comparing multiple groups
- Kruskal–Wallis test as a non-parametric alternative
- Outlier detection
- Distribution normality checking
- Unit tests for statistical functions
- Command-line interface

---

# How It Works

The user provides a CSV file and specifies the type of data.

The program then:

1. Reads the data from the CSV file.
2. Determines the number of groups and data categories.
3. Prepares the data for analysis.
4. Selects an appropriate statistical method.
5. Performs the statistical test.
6. Compares the calculated statistic with a critical value or calculates a p-value.
7. Determines whether the observed difference is statistically significant.

For quantitative data, the program additionally checks:

- whether the data contains outliers;
- whether the distribution is approximately normal.

These checks are used to select either a parametric or a non-parametric statistical method.

---

#  Statistical Methods

| Data type | Conditions | Method |
|-----------|------------|--------|
| Categorical | 2 groups × 2 categories | Z-test |
| Categorical | More complex contingency table | χ² test |
| Quantitative | 2 groups, normal distribution, no outliers | Welch’s t-test |
| Quantitative | More than 2 groups, normal distribution, no outliers | ANOVA |
| Quantitative | Non-normal distribution or outliers | Kruskal–Wallis test |

The application selects a statistical approach according to the structure of the input data.

---

# Project Structure

data_analytics/
│
├── main.py              # Application entry point and CLI argument parsing
├── data_input.py        # Input data loading and preparation
├── statistics.py        # Statistical method selection
├── tests.py             # Statistical test implementations
├── unit_tests.py        # Unit tests for statistical functions
├── critical_values.py   # Critical value tables
├── utils.py             # Utility functions
│
└── data.csv             # Input CSV file

The project is divided into separate modules responsible for:

1) input data
2) statistical logic
3) statistical tests
4) testing
5) application execution

---

# To make the code work, you need to install the libraries: 

1) pandas
2) numpy
3) os

---

# Example of categorical data

Group,Bought,Did not buy
A,100,900
B,120,880
C,130,870

In this example:

A, B, C are experimental groups;
Bought is the number of users who performed the target action;
Did not buy is the number of users who did not perform the target action.

For categorical data, the program calculates the Total column automatically, so you do not need to add this column to the data yourself.

---

# Running the Application

- For categorical data:

python main.py --file data.csv --type categorical

- For quantitative data:

python main.py --file data.csv --type quantitative

- For Z-test:

When the data contains two groups and two categories, the program uses a Z-test to compare conversion rates.
For example:

python main.py --file data.csv --type categorical --column 1 --alternative one-sided

or:

python main.py --file data.csv --type categorical --column 1 --alternative two-sided
--column

Specifies which category should be analyzed.
For example:

--column 1

means that the first category will be analyzed.

--alternative

Two alternatives are supported:

one-sided;
two-sided.

---

# Unit Tests

The project contains a separate unit_tests.py module with test datasets and checks for the statistical functions.
The unit tests cover:

Z-test;
χ² test;
Welch's t-test;
ANOVA;
Kruskal–Wallis test;
normality checking;
outlier detection.

Run the unit tests with:

python main.py --file data.csv --type categorical --unit-test

---

# What This Project Demonstrates

This project provides practice with several areas of Python and data analysis:

Python programming;
modular code organization;
CSV processing;
Pandas DataFrames;
statistical analysis;
A/B testing;
statistical hypothesis testing;
critical value tables;
command-line interfaces;
unit testing.

---

# Limitations

This is an educational project and is not intended to replace professional statistical software.
When applying the results to a real-world A/B test, additional factors should be considered, including:

sample size;
statistical power;
significance level (in this programm it is equal to 0.05);
multiple comparisons;
assumptions of the selected statistical test.

---

# Possible Improvements

Future versions could include:

 migrate to pytest;
 automatically determine the appropriate test without manual parameters;
 improve CSV validation and error handling;
 support additional data formats;
 add result visualizations;
 add confidence intervals;
 add effect size calculations;
 add logging;
 add requirements.txt;
 improve the unit test structure.

---

# Author

Vasily Orlov

GitHub:
https://github.com/Vasliy-Vasily
