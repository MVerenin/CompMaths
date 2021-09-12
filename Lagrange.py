import numpy as np
import matplotlib.pyplot as plt

class Lagrange:
    def __init__(self, ArrX, ArrF, x):
        self.ArrX = ArrX
        self.ArrF = ArrF
    def Interpolation(self, x):
        P=0
        for k in range(len(self.ArrX)):
            NewArr1 = x*np.ones(len(self.ArrX)) - self.ArrX
            NewArr2 = self.ArrX[k]*np.ones(len(self.ArrX)) - self.ArrX
            NewArr2[k]=1
            NewArr1[k]=1
            P += np.prod(NewArr1)/np.prod(NewArr2)*self.ArrF[k]
        return P
    
