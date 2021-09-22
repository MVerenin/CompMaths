import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Класс сплайна
class CubicSpline:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x
 
# Построение сплайна
# x - узлы сетки
# y - значения функции в узлах сетки
# n - количество узлов сетки
def solveTriagonalSlae(x, y, n):
    # Инициализация массива сплайнов
    splines = [CubicSpline(0, 0, 0, 0, 0) for _ in range(0, n)]
    for i in range(0, n):
        splines[i].x = x[i]
        splines[i].a = y[i]
    
    splines[0].c = splines[n - 1].c = 0.0
    
    # Решение СЛАУ относительно коэффициентов методом прогонки
    # Прямой ход
    alpha = [0.0 for _ in range(0, n - 1)]
    beta  = [0.0 for _ in range(0, n - 1)]
 
    for i in range(1, n - 1):
        hi  = x[i] - x[i - 1]
        hi1 = x[i + 1] - x[i]
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z
  
 
    # Обратный ход
    for i in range(n - 2, 0, -1):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]
    
    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
    return splines
 
 
# Вычисление значения интерполированной функции в произвольной точке
def Interpolate(splines, x):
    if not splines:
        return None
    
    n = len(splines)
    s = CubicSpline(0, 0, 0, 0, 0)
    
    if x <= splines[0].x: # Если x меньше точки сетки x[0] - пользуемся первым эл-тов массива
        s = splines[0]
    elif x >= splines[n - 1].x: # Если x больше точки сетки x[n - 1] - пользуемся последним эл-том массива
        s = splines[n - 1]
    else: # Иначе x лежит между граничными точками сетки - производим бинарный поиск нужного эл-та массива
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            if x <= splines[k].x:
                j = k
            else:
                i = k
        s = splines[j]
    
    dx = x - s.x
    # Вычисляем значение сплайна в заданной точке по схеме Горнера
    return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx;
    


lis = pd.read_csv('Atmosphere_1.csv', names = ['H', 'DEN'])
h=list(lis.H)
den=list(lis.DEN)
del h[0]
del den[0]
high=list(map(float,h))
density=list(map(float,den))

spline = solveTriagonalSlae(high, density, len(high))

graphX = np.linspace(high[0],high[len(high)-1],500)
graphY = []
for i in range (500):
    graphY.append(Interpolate(spline, graphX[i]))
for i in range (500):
    if graphY[i]<2*10**-8:
        print(graphX[i])
        break
plt.plot(graphX, graphY, color='yellow')
plt.scatter(high,density,color='black')
plt.show()
