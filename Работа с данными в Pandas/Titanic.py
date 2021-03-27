import bs4
import pandas as pd
import numpy as np
from beauty_print import beauty_print

titanic_full_df = pd.read_csv("https://github.com/agconti/kaggle-titanic/raw/master/data/train.csv", sep=",")

# Общее представление работы с данными
#beauty_print("Размер:", titanic_full_df.shape)

#print("Инфо:")
#titanic_full_df.info()

#beauty_print("Описание:", titanic_full_df.describe())
#beauty_print("Наименования колонок:", titanic_full_df.columns)
#beauty_print("Типы данных по колонкам:", titanic_full_df.dtypes)
#beauty_print("Начальные данные:", titanic_full_df.head())
#beauty_print("Конечные данные:", titanic_full_df.tail(7))
#beauty_print("Количество ячеек с NULL'ом:", titanic_full_df.isnull().sum())
#beauty_print("Рандомные 5 строк таблицы:", titanic_full_df.sample(5))

# Индексация и выделение данных
#beauty_print("Определённая колонка + только начальные данные:", titanic_full_df["Age"].head())
#beauty_print("Тип у колонки в DataFrame:", type(titanic_full_df["Age"]))
#beauty_print("2 колонки + только начальные данные:", titanic_full_df[["Age", "Sex"]].head())

#Работа с новой колонкой в DataFrame
titanic_full_df["Relatives"] = titanic_full_df["SibSp"] + titanic_full_df["Parch"]
#beauty_print("Вывод новой колонки с двумя старыми:", titanic_full_df[["SibSp", "Parch", "Relatives"]].head())
#beauty_print("Удаление 3й строчки (с индексом 2):", titanic_full_df.drop(2, axis=0).head())
#beauty_print("Удаление столбца с названием 'Relatives':", titanic_full_df.drop("Relatives", axis=1).head())

#beauty_print("Получение первых 10 индексов из DataFrame в виде листа:", titanic_full_df.index.tolist()[:10])
#beauty_print("Получение данных из определённых индексов и колонок:", titanic_full_df.loc[442 : 450 : 2, ["Age", "Sex"]])
#beauty_print("Установка колонки в качестве индекса и выборка по значению индекса:", titanic_full_df.set_index(["Embarked"]).loc["S"].head())
#beauty_print("Получение значений у первой строки:", titanic_full_df.iloc[0])
#beauty_print("Получение данных из определённых индексов:", titanic_full_df.iloc[[564, 442]])
#beauty_print("Получение данных из определённых индексов и колонок (2):", titanic_full_df.loc[[564, 442], ["Name", "Sex"]])
#beauty_print("Проверка значений каждой ячейки на равенство единицы:", titanic_full_df == 1)
#beauty_print("Проверка значений каждой ячейки в колонке 'Survived':", (titanic_full_df.Survived == 1).head())
#beauty_print("Получение таблицы, в которой поле 'Survived' равно 0:", titanic_full_df[titanic_full_df["Survived"] == 0].head())
#beauty_print("Получение количества элементов с одинаковыми значениями в таблице 'Sex', с учётом, что 'Survived' равно 1:", titanic_full_df[titanic_full_df["Survived"] == 1]["Sex"].value_counts())
#beauty_print("Получение таблицы с 'Fare > 100' или 'Name' содержащим 'Master':", titanic_full_df[(titanic_full_df["Fare"] > 100) | (titanic_full_df["Name"].str.find("Master") != -1)].head())

# Методы
#beauty_print("Получение списка всех значений колонки 'Embarked':", titanic_full_df["Embarked"].unique())
#beauty_print("Получение количества всех различных значений колонки 'Embarked':", titanic_full_df["Embarked"].nunique())
#beauty_print("Получение количества элементов с одинаковыми значениями в таблице 'Survived':", titanic_full_df["Survived"].value_counts())
#beauty_print("Получение количества элементов с одинаковыми значениями в таблице 'PClass':", titanic_full_df["Pclass"].value_counts())

# Замена значений [1,2,3] колонки 'Pclass' на текст
titanic_full_df["Pclass"].replace({1: "Элита", 2: "Средний класс", 3: "Работяги"}, inplace=True)
#beauty_print("Получение количества элементов с одинаковыми значениями в таблице 'PClass' (2):", titanic_full_df["Pclass"].value_counts())

#beauty_print("Замена значений колонки 'Fare' на 'Дёшево' или 'Дорого' в зависимости от значения:", titanic_full_df["Fare"].apply(lambda x: "Дёшево" if x < 20 else "Дорого"))

# Заполнение новой колонки 'Fare_Bin' в зависимости от значения ячейки 'Fare'
titanic_full_df["Fare_Bin"] = titanic_full_df["Fare"].apply(lambda x: "Дёшево" if x < 20 else "Дорого")
#beauty_print("Произвести сортировку таблицы по полю 'Name':", titanic_full_df.sort_values(by='Name'))

# Работа с пропущенными значениями
#beauty_print("Имеются ли NULL в колонках? :", titanic_full_df.isnull().any())
#beauty_print("Получение таблицы без строк, в которых имеются пропущенные значения:", titanic_full_df.dropna())
#beauty_print("Получение таблицы без строк, в которых имеются пропущенные значения в колонках 'Age' и 'Sex':", titanic_full_df.dropna(subset=["Age", "Sex"]))
#beauty_print("Получение таблицы со строками, где не менее 14 заполненных колонок:", titanic_full_df.dropna(thresh=14))
#beauty_print("Вставка слова 'ПРОПУСК' в ячейки с пропущенными значениями:", titanic_full_df.fillna("ПРОПУСК"))
#beauty_print("Заполнение пустых ячеек в колонке 'Age' средним значением по таблице:", titanic_full_df["Age"].fillna(value=titanic_full_df["Age"].mean()))

# Работа с объединениями
#beauty_print("Получение таблицы количества выживших и погибших мужчин и женщин:", titanic_full_df[["Sex", "Survived"]].pivot_table(index=["Sex"], columns=["Survived"], aggfunc=len))
#beauty_print("Получение таблицы среднего возраста выживших и погибших мужчин и женщин:", titanic_full_df[["Sex", "Survived", "Age"]].pivot_table(values=["Age"], index=["Sex"], columns=["Survived"], aggfunc="mean"))
#beauty_print("Произвести группировку по колонке Pclass и выбрать максимальное значение из каждой группы:", titanic_full_df[titanic_full_df.groupby("Pclass")["PassengerId"].transform(max) == titanic_full_df["PassengerId"]])
#beauty_print("Получение среднего возраста каждого из объединения колонки Pclass:", titanic_full_df.groupby("Pclass").mean()["Age"])
#beauty_print("Получение статистических данных (count, mean, std, min/max, 25%, 50%, 75%) по возрасту в каждом объединении колонки Pclass:", titanic_full_df.groupby("Pclass").describe()["Age"])
#beauty_print("Поменять колонки и строки местами (транспонирование) (пример с прошлым запросом):", titanic_full_df.groupby("Pclass").describe()["Age"].transpose())
#beauty_print("Получение mix/max/std по возрасту по каждому из объединений колонки Pclass:", titanic_full_df.groupby("Pclass")["Age"].agg(["min", "max", "std"]))
#beauty_print("Получение среднего возраста пассажиров и их количество по каждому из объединений колонки Pclass:", titanic_full_df.groupby("Pclass").agg({"Age": np.mean, "PassengerId": "count"}))
#beauty_print("Получение среднего показателя 'Fare' по каждому из объединений колонкок Pclass и Sex одновременно:", titanic_full_df.groupby(["Pclass", "Sex"]).mean()["Fare"])

# Цикл по значениям
#print("Отображение индекса и значение колонки 'Name':")
#for index, row in titanic_full_df.iterrows():
#    print("Index: {}, Name: {}".format(index, row["Name"]))

#print("Отображение наименования объединения групп 'Pclass' и средний возраст:")
#for group_name, group in titanic_full_df.groupby("Pclass"):
#    print(group_name, group["Age"].mean())