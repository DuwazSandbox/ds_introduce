import pandas as pd
import numpy as np
from datetime import datetime, time

la_crimes = pd.read_csv("la-crimes-sample.csv", sep=",")

# 1) Создайте новую колонку, где будет храниться время и дата совершения преступления в подходящем формате. 1101 => 11:01 am
# Своё решение (на коленке)
hoursOccurred = la_crimes['Time Occurred'] // 100
la_crimes['Time Occurred Civilian'] = ((hoursOccurred + 11) % 12 + 1).apply(str) + ":" + (la_crimes['Time Occurred'] % 100).apply(str) + " " + hoursOccurred.apply(lambda x: "pm" if x > 12 else "am")

# Ожидаемое решение
def parse_military_time(mtime):
    minutes = int(str(mtime)[-2:])
    hours = str(mtime)[:-2]
    hours = int(hours) if hours else 0
    return time(hours, minutes)

la_crimes["Time Occurred Civilian"] = la_crimes["Time Occurred"].apply(parse_military_time)

# 2) В какое время суток уровень преступности наивысший?