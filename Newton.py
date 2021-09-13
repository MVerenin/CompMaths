import numpy as np
from sympy import symbols, expand

class Newton:
    def __init__(self, ArrX, ArrF):
        self.ArrX = ArrX #узлы интерполяции
        self.ArrF = ArrF #значения неизвестной функции в узлах интерполяции
    def Coef(self):
        m = len(self.ArrX)
        ArrX = np.copy(self.ArrX)
        Arr = np.copy(self.ArrF)
        for k in range(1, m):
            Arr[k:m] = (Arr[k:m] - Arr[k - 1])/(ArrX[k:m] - ArrX[k - 1]) #вычисляем разделенные разности
        return Arr
    def Polynomial(self):
        x = symbols("x")
        a = self.Coef()
        n = len(self.ArrX) - 1
        p = a[n]
        for k in range(1, n + 1):
            p = a[n - k] + (x - self.ArrX[n - k])*p
        p = p.expand()
        coeffic = []
        for k in range(len(self.ArrX)):
            coeffic.append(p.coeff(x,k))
        return coeffic
    def Interpolation(self, x):
        PN = 0
        for k in range(len(self.ArrX)):
            PN += self.Polynomial()[k]*x**k
        return PN   
