import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams

import pandas as pd

sns.set_style("ticks")
rcParams['figure.figsize'] = 12, 6

# График по значениям Series
ser2 = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])
#ser2.plot()
#plt.show()

# Гистограмма по значениям Series
#ser2.plot(kind="bar", fontsize=20)
#plt.show()

# Гистограмма по каждой колонке из DataFrame
titanic_full_df = pd.read_csv("https://github.com/agconti/kaggle-titanic/raw/master/data/train.csv", sep=",")
#titanic_full_df.hist()
#plt.show()

# График плотности распределения пассажиров по годам. xlim - ограничения значений по оси X
#titanic_full_df["Age"].plot.kde(xlim=(titanic_full_df["Age"].min(), titanic_full_df["Age"].max()))
#plt.show()

# Круговая диаграмма с пассажирами на борту Титаника разделённая по половому признаку
#titanic_full_df["Sex"].value_counts().plot(kind="pie", figsize=(7, 7), fontsize=20)
#plt.show()

# Объединение двух графиков. Гистограммы выживших и нет по половому признаку
#titanic_full_df[["Sex", "Survived"]].pivot_table(index=["Sex"], columns=["Survived"], aggfunc=len).plot(kind="bar")
#plt.show()

# Объединение двух графиков. Графики выживших и нет по количеству лет
#titanic_full_df[["Age", "Survived"]].pivot_table(index=["Age"], columns=["Survived"], aggfunc=len).plot()
#plt.show()
