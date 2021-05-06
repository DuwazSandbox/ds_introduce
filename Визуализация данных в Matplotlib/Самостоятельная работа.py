import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2

# Задача 1
# Создайте объект класса Figure используя метод plt.figure()
#fig = plt.figure()
# Используйте add_axes чтобы добавить оси, занимающие все полотно фигуры.
#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# Изобразите на полученном графике связь между x и y.
#axes.plot(x, y, 'b')
#axes.set_xlabel('Ось X')
#axes.set_ylabel('Ось Y')
#axes.set_title('Заголовок');
#plt.show()

# Задача 2
# Создайте на одном полотне две пары осей
#fig = plt.figure()
#axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#axes2 = fig.add_axes([0.6, 0.5, 0.15, 0.15])
# Визуализируйте данные на каждой паре осей как указано на рисунке
#axes1.plot(x, y, 'b')
#axes1.set_xlabel('x')
#axes1.set_ylabel('y')
#axes2.plot(x, y, 'b')
#axes2.set_xlabel('x')
#axes2.set_ylabel('y')
#plt.show()

# Задача 3
# Напишите код, чтобы получить похожие графики
#fig, axes = plt.subplots(1, 2, figsize=(10, 3))
#axes[0].plot(x, y, 'b', linewidth=5.00)
#axes[0].set_xlabel('x')
#axes[0].set_ylabel('y')
#axes[1].plot(x, z, 'r--')
#axes[1].set_xlabel('x')
#axes[1].set_ylabel('z')
#plt.tight_layout()
#plt.show()