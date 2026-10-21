[Русская версия](#статистический-анализ-ab-теста)

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

```
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
```

The project is divided into separate modules responsible for:

1. Input data  
2. Statistical logic  
3. Statistical tests  
4. Testing  
5. Application execution

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
 
```
python main.py --file data.csv --type categorical
```

- For quantitative data:

```
python main.py --file data.csv --type quantitative
```

- For Z-test:

When the data contains two groups and two categories, the program uses a Z-test to compare conversion rates.
For example:

```
python main.py --file data.csv --type categorical --column 1 --alternative one-sided
```

or:

```
python main.py --file data.csv --type categorical --column 1 --alternative two-sided
--column
```

Specifies which category should be analyzed.
For example:

```
--column 1
```

means that the first category will be analyzed.

```
--alternative
```

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

Unit tests can be run separately from data analysis.
Run the unit tests with:

```
python main.py --unit-test
```

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

---

# Статистический анализ A/B-теста

Приложение на Python с командной строкой для статистического анализа результатов A/B-теста.
Программа принимает данные из CSV-файла, определяет подходящий статистический тест в зависимости от типа данных и структуры эксперимента, выполняет необходимые расчёты
и сообщает, является ли наблюдаемое различие статистически значимым.
Проект создан в образовательных целях для практики Python, статистического анализа, Pandas, проверки гипотез и модульной организации кода.

[English version](#statistical-analysis-of-an-ab-test)

---

# Возможности

- Загрузка данных из CSV-файлов
- Поддержка категориальных и количественных данных
- Автоматический выбор статистического метода
- Z-тест для сравнения конверсий
- Тест хи-квадрат (χ²) для категориальных данных
- t-тест Уэлча для количественных данных
- ANOVA для сравнения нескольких групп
- Тест Краскела–Уоллиса как непараметрическая альтернатива
- Обнаружение выбросов
- Проверка нормальности распределения
- Юнит-тесты для статистических функций
- Интерфейс командной строки

---

# Как это работает

Пользователь передаёт CSV-файл и указывает тип данных.

Далее программа:

1. Читает данные из CSV-файла.
2. Определяет количество групп и категорий данных.
3. Подготавливает данные к анализу.
4. Выбирает подходящий статистический метод.
5. Выполняет статистический тест.
6. Сравнивает вычисленную статистику с критическим значением или рассчитывает p-value.
7. Определяет, является ли наблюдаемое различие статистически значимым.

Для количественных данных программа дополнительно проверяет:

- содержит ли выборка выбросы;
- является ли распределение приблизительно нормальным.

Эти проверки используются для выбора параметрического или непараметрического метода.

---

# Статистические методы

| Тип данных | Условия | Метод |
|-----------|---------|-------|
| Категориальные | 2 группы × 2 категории | Z-тест |
| Категориальные | Более сложная таблица сопряжённости | χ²-тест |
| Количественные | 2 группы, нормальное распределение, без выбросов | t-тест Уэлча |
| Количественные | Больше 2 групп, нормальное распределение, без выбросов | ANOVA |
| Количественные | Ненормальное распределение или выбросы | Тест Краскела–Уоллиса |

Программа выбирает статистический подход в соответствии со структурой входных данных.

---

# Структура проекта

```
data_analytics/
│
├── main.py              # Точка входа и разбор аргументов командной строки
├── data_input.py        # Загрузка и подготовка входных данных
├── statistics.py        # Выбор статистического метода
├── tests.py             # Реализация статистических тестов
├── unit_tests.py        # Юнит-тесты для статистических функций
├── critical_values.py   # Таблицы критических значений
├── utils.py             # Вспомогательные функции
│
└── data.csv             # Входной CSV-файл
```

Проект разделён на отдельные модули, отвечающие за:

1. Входные данные
2. Статистическую логику
3. Статистические тесты
4. Тестирование
5. Запуск приложения

---

# Чтобы код работал, нужно установить библиотеки:

1) pandas
2) numpy
3) os

---

# Пример категориальных данных

Group,Bought,Did not buy
A,100,900
B,120,880
C,130,870

В этом примере:

A, B, C — экспериментальные группы;
Bought — количество пользователей, совершивших целевое действие;
Did not buy — количество пользователей, не совершивших целевое действие.

Для категориальных данных программа автоматически вычисляет столбец Total, поэтому добавлять его вручную не нужно.

---

# Запуск приложения

- Для категориальных данных:

```
python main.py --file data.csv --type categorical
```

- Для количественных данных:

```
python main.py --file data.csv --type quantitative
```

- Для Z-теста:

Когда в данных две группы и две категории, программа использует Z-тест для сравнения конверсий.
Например:

```
python main.py --file data.csv --type categorical --column 1 --alternative one-sided
```

или:

```
python main.py --file data.csv --type categorical --column 1 --alternative two-sided
--column
```

Указывает, какую категорию анализировать.
Например:

```
--column 1
```

означает, что будет анализироваться первая категория.

```
--alternative
```

Поддерживаются два варианта:

one-sided;
two-sided.

---

# Юнит-тесты

В проекте есть отдельный модуль unit_tests.py с тестовыми наборами данных и проверками статистических функций.
Юнит-тесты покрывают:

Z-тест;
χ²-тест;
t-тест Уэлча;
ANOVA;
тест Краскела–Уоллиса;
проверку нормальности;
обнаружение выбросов.

Юнит-тесты можно запускать отдельно от анализа данных.
Запуск юнит-тестов:

```
python main.py --unit-test
```

---

# Что демонстрирует проект

Проект даёт практику в нескольких областях Python и анализа данных:

программирование на Python;
модульная организация кода;
обработка CSV;
Pandas DataFrame;
статистический анализ;
A/B-тестирование;
проверка статистических гипотез;
таблицы критических значений;
интерфейс командной строки;
юнит-тестирование.

---

# Ограничения

Это образовательный проект, и он не предназначен для замены профессионального статистического ПО.
При применении результатов к реальному A/B-тесту следует учитывать дополнительные факторы, включая:

размер выборки;
статистическую мощность;
уровень значимости (в этой программе он равен 0.05);
множественные сравнения;
предпосылки выбранного статистического теста.

---

# Возможные улучшения

В будущих версиях можно:

 перейти на pytest;
 автоматически определять подходящий тест без ручных параметров;
 улучшить валидацию CSV и обработку ошибок;
 поддержать дополнительные форматы данных;
 добавить визуализацию результатов;
 добавить доверительные интервалы;
 добавить расчёт размера эффекта;
 добавить логирование;
 добавить requirements.txt;
 улучшить структуру юнит-тестов.

---

# Автор

Василий Орлов

GitHub:
https://github.com/Vasliy-Vasily
