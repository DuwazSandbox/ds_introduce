from beauty_print import beauty_print

# Стандартная работа со временем
import datetime

today = datetime.datetime.today()
#beauty_print("Сегодняшний день:", today)

#beauty_print("Какой сегодня год?", today.year)
#beauty_print("Какой сегодня месяц?", today.month)
#beauty_print("Какой сегодня день?", today.day)

# Разные способы представления вывода даты
#beauty_print("Представление ввиде строки:", today.ctime())
#beauty_print("Представление ввиде tuple:", today.timetuple())
#beauty_print("Количество дней с 01.01.01:", today.toordinal())

#beauty_print("Разница между datetime:", today.replace(today.year + 1) - today)
#beauty_print("Добавление к дате определённую разницу во времени:", today + datetime.timedelta(days=1000))

# -------------

import pandas as pd
import numpy as np
from datetime import datetime

#beauty_print("Генерация 10 дат с разницей в 1 день:", pd.date_range('1/1/2000', periods=10, freq="D"))
#beauty_print("Генерация 10 дат с разницей в 3 дня:", pd.date_range('1/1/2000', periods=10, freq="3D"))

start = datetime(2011, 1, 1)
end = datetime(2012, 1, 1)
#beauty_print("Генерация дат концов месяцев в указанном промежутке времени:", pd.date_range(start, end, freq="BM"))
#beauty_print("Генерация дат с указанным окончанием последовательности:", pd.date_range(end=end, periods=5))

#beauty_print("Генерация дат с указанием последовательности дней в виде чисел:", pd.to_datetime([1, 2, 3, 0], unit='D', origin=datetime(2012, 5, 3)))

#beauty_print("Конвертация Series строк в datetime:", pd.to_datetime(pd.Series(['2000-01-01', 'Jul 31, 2009', '10/01/2010', '10 12 2011'])))

# Генерация DataFrame с индексами в виде дат
ts_df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C'],
    index=pd.date_range('1/1/2000', periods=10))

#beauty_print("Вывод сгенерированного DataFrame с индексами в виде дат:", ts_df)
#beauty_print("Работа с индексами DataFrame, как с датами", ts_df["2000-01":"2000-01-09":2])
#beauty_print("Получение данных с 6-часовым периодом", ts_df.asfreq("6H").head())
#beauty_print("Получение данных с 6-часовым периодом с заполнением NULL-ячеек предыдущими значениями", ts_df.asfreq("6H", method="pad").head(6))
#beauty_print("Получение средних значений за 3 дня", ts_df.resample("3D").mean())

# Сброс значений индексов с созданием колонки "index" в DataFrame
ts_df.reset_index(inplace=True)
# Переименование названия колонки
ts_df.rename(columns={"index": "date"}, inplace=True)
#beauty_print("Вывод DataFrame с перемещённым значением индексов в качестве колонки", ts_df)

#beauty_print("Получение данных отфильтрованных по дате (позже 04.01.2000)", ts_df[(ts_df["date"] > datetime(2000, 1, 4))])
#beauty_print("Получение данных отфильтрованных по дате (4 и 5 день месяца)", ts_df[(ts_df["date"].dt.day > 3) & (ts_df["date"].dt.day < 6)])
#beauty_print("Получение данных отфильтрованных по дате (только суббота (пн=0, вс=6))", ts_df[(ts_df["date"].dt.weekday == 5)])
