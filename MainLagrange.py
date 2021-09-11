import Lagrange as L
import matplotlib.pyplot as plt
import numpy as np

print ("Введите координаты узлов интерполяции")

ArrX = list(map(float,input().split()))

print ("Введите значения неизвестной функции в узлах")

ArrF = list(map(float,input().split()))

print ("Введите число точек для построения графика")

N = int(input())

l = L.Lagrange(ArrX, ArrF, N)

VecX = np.linspace(min(ArrX), max(ArrX), N)
VecY = l.Interpolation()
plt.scatter(ArrX, ArrF, color = 'Yellow')
plt.plot(VecX, VecY, color = 'Black')
plt.show()

