import numpy as np
from sympy import symbols, expand

class Lagrange:
    def __init__(self, ArrX, ArrF):
        self.ArrX = ArrX
        self.ArrF = ArrF
    def Polynomial(self):
        x = symbols("x")
        P = 0
        coef = []
        for k in range(len(self.ArrX)):
            NewArr1 = x*np.ones(len(self.ArrX)) - self.ArrX
            NewArr2 = self.ArrX[k]*np.ones(len(self.ArrX)) - self.ArrX
            NewArr2[k]=1
            NewArr1[k]=1
            P += np.prod(NewArr1)/np.prod(NewArr2)*self.ArrF[k]
            P = P.expand()
        for k in range(len(self.ArrX)):
            coef.append(P.coeff(x,k))
        return coef
    def Interpolation(self, x):
        PL = 0
        for k in range(len(self.ArrX)):
            PL += self.Polynomial()[k]*x**k
        return PL    

