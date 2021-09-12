import numpy as np

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
    def Interpolation(self, x):
        a = self.Coef()
        n = len(self.ArrX) - 1
        p = a[n]
        for k in range(1, n + 1):
            p = a[n - k] + (x - self.ArrX[n - k])*p
        return p
