import pandas as pd
import matplotlib.pyplot as plt

from beauty_print import beauty_print

la_crimes = pd.read_csv("la-crimes-sample.csv", sep=",")

#beauty_print("Размерность таблицы:", la_crimes.shape)
#beauty_print("Наименования колонок:", la_crimes.columns)
#beauty_print("Типы данных у колонок:", la_crimes.dtypes)
#beauty_print("Количество уникальных значений в колонках:", la_crimes.nunique())
#beauty_print("Количество пропущенных значений в колонках:", la_crimes.isnull().sum())

# Жертвы
# Круговая диаграмма по происхождению жертвы
#la_crimes["Victim Descent"].replace({'A': "Other Asian", 'B': "Black", 'C': "Chinese", 
#    'D': "Cambodian", 'F': "Filipino", 'G': "Guamanian", 'H': "Hispanic/Latin/Mexican",
#    'I': "American Indian/Alaskan Native", 'J': "Japanese", 'K': "Korean", 'L': "Laotian",
#    'O': "Other", 'P': "Pacific Islander", 'S': "Samoan", 'U': "Hawaiian", 'V': "Vietnamese",
#    'W': "White", 'X': "Unknown", 'Z': "Asian Indian"}, inplace=True)
#la_crimes["Victim Descent"].value_counts().plot(kind="pie", figsize=(7, 7), fontsize=20)
#plt.show()

# Круговая диаграмма по половому признаку жертвы
#la_crimes["Victim Sex"].value_counts().plot(kind="pie", figsize=(7, 7), fontsize=20)
#plt.show()

# Преступления, пол и возраст
# Распределение по возрасту жертвы
#la_crimes["Victim Age"].plot.kde(xlim=(la_crimes["Victim Age"].min(), la_crimes["Victim Age"].max()))
#plt.show()
#la_crimes["Victim Age"].hist()
#plt.show()

# График вероятности становления жертвой по возрасту и полу жертвы
#la_crimes[["Victim Age", "Victim Sex"]].pivot_table(index=["Victim Age"], columns=["Victim Sex"], aggfunc=lambda x: x.shape[0]/la_crimes.shape[0]).plot()
#plt.show()

# 10 самых распространенных преступлений в LA
#most_crimes = la_crimes.groupby("Crime Code")["Crime Code"].count().sort_values(ascending=False).head(10)
#most_crimes.plot(kind="bar")
#plt.show()

# Самый популярный Crime code при жертве женского пола
#print(la_crimes[la_crimes["Victim Sex"] == 'F']["Crime Code"].mode()[0])
# Самый популярный Crime code при жертве мужского пола
#print(la_crimes[la_crimes["Victim Sex"] == 'M']["Crime Code"].mode()[0])
# Возможно также и так
#print(la_crimes[["Crime Code", "Victim Sex"]].groupby("Victim Sex").apply(pd.DataFrame.mode))

# Место происшествия
# График количества преступлений по районам
#la_crimes.groupby("Area ID")["Area ID"].count().sort_values().plot(kind="bar")
#plt.show()

#print(la_crimes[["Area ID", "Victim Descent"]].groupby("Area ID").apply(pd.DataFrame.mode))