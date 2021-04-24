import pandas as pd
import numpy as np
from datetime import datetime, time

la_crimes = pd.read_csv("la-crimes-sample.csv", sep=",")

# 1) Создайте новую колонку, где будет храниться время и дата совершения преступления в подходящем формате. 1101 => 11:01 am
# 1.1) Своё решение (на коленке) (Как понял курс)
#hoursOccurred = la_crimes['Time Occurred'] // 100
#la_crimes['Occurred Civilian'] = ((hoursOccurred + 11) % 12 + 1).apply(str) + ":" + (la_crimes['Time Occurred'] % 100).apply(str) + " " + hoursOccurred.apply(lambda x: "pm" if x > 12 else "am")

# 1.2) Видимо, ожидаемое решение (хоть и не соответствует задаче)
def parse_military_time(mtime):
    minutes = int(str(mtime)[-2:])
    hours = str(mtime)[:-2]
    hours = int(hours) if hours else 0
    return time(hours, minutes)

la_crimes["Time Occurred Civilian"] = la_crimes["Time Occurred"].apply(parse_military_time)

# 1.3) Немного переделанный свой код
#def convert_to_military_time(mtime):
#    if mtime == 1200:
#        return "Noon"
#    if mtime == 2400:
#        return "12 Midnight"
#    minutes = mtime % 100
#    hours = mtime // 100
#    printable_hours = (hours - 1) % 12 + 1 # from 1 to 12
#    post_meridiem = (hours >= 12)
#    return "{:02d}".format(printable_hours) + ":" + "{:02d}".format(minutes) + " " + ("pm" if post_meridiem else "am")
    
#la_crimes["Occurred Civilian"] = la_crimes["Time Occurred"].apply(convert_to_military_time)

# 2) В какое время суток уровень преступности наивысший?
def convert_to_part_of_day(mtime):
    hours = mtime // 100
    if hours >= 5 and hours < 12:
        return "Morning"
    if hours >= 12 and hours < 17:
        return "Afternoon"
    if hours >= 17 and hours < 21:
        return "Evening"
    return "Night"

la_crimes["Part of Day"] = la_crimes["Time Occurred"].apply(convert_to_part_of_day)
#print(la_crimes["Part of Day"].mode()[0])

### Подготовка данных
la_crimes['Date Occurred'] = pd.to_datetime(la_crimes['Date Occurred'])

# 3) В какой день недели происходит наибольшее количество преступлений?
#la_crimes["Part of Day"] = la_crimes['Date Occurred'].dt.day_name()
#print(la_crimes["Part of Day"].mode()[0])

# 4) Постройте график, показывающий распределение количества преступлений в каждый из дней недели.
import seaborn as sns
import matplotlib.pyplot as plt

#sns.violinplot(
#    x=la_crimes["Date Occurred"].dt.day_name(),
#    y=la_crimes["Time Occurred Civilian"].apply(lambda t: t.hour),
#    palette='rainbow')
#plt.ylim(0, 23)
#plt.show()

# 5) Постройте графики распределения количества преступлений по времени суток для мужчин и женщин.
#pivot_sex_and_part_of_day=la_crimes[["Part of Day","Victim Sex"]].pivot_table(index=["Part of Day"], columns=["Victim Sex"], aggfunc=len)
#pivot_sex_and_part_of_day.drop(pivot_sex_and_part_of_day.columns.difference(['F','M']), 1, inplace=True)
#pivot_sex_and_part_of_day.plot()
#plt.show()

# 6) Какие виды преступлений чаще совершаются днём, а какие ночью?
# Не придумал иначе
#la_crimes["Day or Night"] = la_crimes["Time Occurred Civilian"].apply(lambda x : "Day" if (x > time(5,00)) & (x < time(23,00)) else "Night")
#print(la_crimes.groupby("Day or Night")["Crime Code"].agg(pd.Series.mode))

# 7) Рассчитайте среднее количество преступлений в каждый из дней. Визуализируйте эту величину и опишите график.
#la_crimes["Day and Month Occurred"] = la_crimes["Date Occurred"].apply(lambda x : '{0:02d}'.format(x.month) + " " + '{0:02d}'.format(x.day))
#group = la_crimes.groupby("Day and Month Occurred")
#all_years = group["Day and Month Occurred"].agg("count")
#uniq_year = group["Date Occurred"].nunique()
#all_years.divide(uniq_year).plot()
#plt.show()

# 8) Сколько дней в среднем проходит с момента совершения преступления до момента поступления информации о его совершении?
#la_crimes['Date Reported'] = pd.to_datetime(la_crimes['Date Reported'])
#print((la_crimes['Date Reported'] - la_crimes['Date Occurred']).mean().days)