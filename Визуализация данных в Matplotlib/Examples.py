import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(0, 5, 11)
y = x**2

# Простое отображение графика
#plt.plot(x, y, 'r')  #  r - значит red
#plt.xlabel('Ось X')
#plt.ylabel('Ось Y')
#plt.title('Заголовок графика')
#plt.show()

# Несколько графиков на одном полотне
#plt.subplot(1, 2, 1) # таблица: 1 строка, 2 столбца, выбор 1й ячейки этой таблицы
#plt.plot(x, y, 'r--') # красная пунктирная линия
#plt.subplot(1, 2, 2)
#plt.plot(y, x, 'g*-') # зелёная линия с точками
#plt.show()

# Объектно-ориентированный стиль создания графиков
#fig = plt.figure() # Создание пустого полотна
# Расположение осей графика относительно нижней левой точки окна. Первые 2 параметра указывают смещения в процентном соотношении от размеров окна
#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # координаты левого нижнего угла, ширина и высота. (range 0 to 1)
#axes.plot(x, y, 'b')
#axes.set_xlabel('Ось X')
#axes.set_ylabel('Ось Y')
#axes.set_title('Заголовок');
#plt.show()

# Создание графика внутри другого графика
#fig = plt.figure()
#axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#axes1.plot(x, y, 'b')
#axes1.set_xlabel('Подпись оси X большого графика')
#axes1.set_ylabel('Подпись оси Y большого графика')
#axes1.set_title('Заголовок большого графика')
#axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
#axes2.plot(y, x, 'r')
#axes2.set_xlabel('Подпись оси X\nмалого графика')
#axes2.set_ylabel('Подпись оси Y\nмалого графика')
#axes2.set_title('Заголовок малого графика')
#plt.show()

# Создание пустого полотна со стандартными значениями "add_axes"
#fig, axes = plt.subplots()
#axes.plot(x, y, 'r')
#axes.set_xlabel('x')
#axes.set_ylabel('y')
#axes.set_title('Заголовок')
#plt.show()

# Несколько графиков на одном полотне (способ 2)
#fig, axes = plt.subplots(nrows=1, ncols=2)
#for ax in axes:
#    ax.plot(x, y, 'g')
#    ax.set_xlabel('x')
#    ax.set_ylabel('y')
#    ax.set_title('Заголовок')
#plt.tight_layout() # для создания неперекрывающихся осей и ylables
#plt.show()

# figsize - указание ширины и высоты графика в дюймах
# dpi - кол-во точек на дюйм
# можно так # fig = plt.figure(figsize=(8,4), dpi=100) 
#fig, axes = plt.subplots(figsize=(8,4), dpi=100) # можно и так
#axes.plot(x, y, 'r')
#axes.set_xlabel('x')
#axes.set_ylabel('y')
#axes.set_title('Заголовок')
#plt.show()

# Сохранение графика
#fig.savefig("plot.png", dpi=200)

# Легенды
#fig, axes = plt.subplots()
#axes.plot(x, x**2, label='x**2')
#axes.plot(x, x**3, label='x**3')
#axes.legend() # производит включение отображения окошка с ледендой
# Различное расположение легенды
#axes.legend(loc=1)  # сверху справа
#axes.legend(loc=2)  # сверху слева
#axes.legend(loc=3)  # снизу слева
#axes.legend(loc=4)  # снизу справа
#plt.show()

# Указание цвета и alpha-канала графика
#fig, axes = plt.subplots()
#axes.plot(x, x+1, color="blue", alpha=0.5) # Полупрозрачная, хоть этого и не видно
#axes.plot(x, x+2, color="#8B008B")
#axes.plot(x, x+3, color="#FF8C00")
#plt.show()

# Стили линий и маркеров
#fig, axes = plt.subplots(figsize=(12,6))
# толщина линии указывается через linewidth или lw (эквиваленты)
#axes.plot(x, x+1, color="red", linewidth=0.25)
#axes.plot(x, x+2, color="red", linewidth=0.50)
#axes.plot(x, x+3, color="red", linewidth=1.00)
#axes.plot(x, x+4, color="red", linewidth=2.00)
# стили линий
#axes.plot(x, x+5, color="green", lw=3, linestyle='-') # Сплошная
#axes.plot(x, x+6, color="green", lw=3, ls='-.') # Дефис с точкой
#axes.plot(x, x+7, color="green", lw=3, ls=':') # Пунктирная с мелким шагом
# можно задать свой стиль линии
#line, = axes.plot(x, x+8, color="black", lw=1.50)
#line.set_dashes([5, 10, 15, 10]) # 5 - длина линии, 10 - длина пропуска, 15 - длина линии, 10 - длина пропуска. Повтор.
# возможные маркеры: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
#axes.plot(x, x+9, color="blue",  lw=3, ls='-', marker='+') # добавляет +
#axes.plot(x, x+10, color="blue", lw=3, ls='--', marker='o') # добавляет жирную точку
#axes.plot(x, x+11, color="blue", lw=3, ls='-', marker='s') # добавляет квадрат
#axes.plot(x, x+12, color="blue", lw=3, ls='--', marker='1') # Любое число добавляет трилистник. Повёрнутый на определённый угол
# размер и цвет маркеров
#axes.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
#axes.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
#axes.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
#axes.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
#plt.show()

# Диапазон значений графика
#fig, axes = plt.subplots(1, 3, figsize=(12, 4))
#axes[0].plot(x, x**2, x, x**3)
#axes[0].set_title("Стандартный диапазон осей")
#axes[1].plot(x, x**2, x, x**3)
#axes[1].axis('tight')
#axes[1].set_title("«Тесные» оси")
#axes[2].plot(x, x**2, x, x**3)
#axes[2].set_ylim([0, 60])
#axes[2].set_xlim([2, 5])
#axes[2].set_title("Заданный точными значениями\nдиапазон осей")
#plt.show()

# Другие типы графиков
# График, где указаны точки {x,y} без из соединений линией
#plt.scatter(x,y)
#plt.show()
# Гистограмма
#from random import sample
#data = sample(range(1, 1000), 100)
#plt.hist(data)
#plt.show()
# Японские свечи
#data = [np.random.normal(0, std, 100) for std in range(1, 4)]
#plt.boxplot(data,vert=True,patch_artist=True)
#plt.show()