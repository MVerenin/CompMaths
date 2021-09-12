import Newton as N
import matplotlib.pyplot as plt
import numpy as np

print ("Введите координаты узлов интерполяции")

ArrX = list(map(float,input().split()))

print ("Введите значения неизвестной функции в узлах")

ArrF = list(map(float,input().split()))

print ("Введите абсциссу точки")

x = float(input())

n = N.Newton(ArrX, ArrF)

print ("Значение интерполянта Ньютона равно ", n.Interpolation(x))

VecX = np.linspace(min(ArrX), max(ArrX), 50)
VecY = []
for k in range (50):
    VecY.append(n.Interpolation(VecX[k]))
plt.scatter(ArrX, ArrF, color = 'Yellow')
plt.plot(VecX, VecY, color = 'Black')
plt.show()

