import pandas as pd
import numpy as np
from beauty_print import beauty_print

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}

# Series – это проиндексированный одномерный массив значений.
# Он похож на простой словарь типа dict, где имя элемента
# будет соответствовать индексу, а значение – значению записи.

print("Series begin!!!")
beauty_print("list:", pd.Series(data=my_list))
beauty_print("list and labels:", pd.Series(data=my_list, index=labels))
beauty_print("arr and labels:", pd.Series(arr, labels))
beauty_print("dict:", pd.Series(d))
beauty_print("funcs:", pd.Series([sum,print,len]))

skiing_points = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
beauty_print("skiing_points:", skiing_points)

dancing_points = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])
beauty_print("dancing_points:", dancing_points)

beauty_print("sum points:", skiing_points + dancing_points)

beauty_print("Germany's ponts:", (skiing_points + dancing_points)['Germany'])
print("Series end!!!")

print("---")

# DataFrame — это проиндексированный многомерный массив значений,
# соответственно каждый столбец DataFrame, является структурой Series.

print("DataFrames begin!!!")

df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
beauty_print("random dataframe:", df)

print("DataFrames end!!!")