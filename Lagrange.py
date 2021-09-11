import numpy as np
import matplotlib.pyplot as plt

class Lagrange:
    def __init__(self, ArrX, ArrF, N):
        self.ArrX = ArrX
        self.ArrF = ArrF
        self.N = N
    def Interpolation(self):
        VecX = np.linspace(min(self.ArrX), max(self.ArrX), self.N)
        PL=[]
        for x in VecX:
            P=0
            for k in range(len(self.ArrX)):
                NewArr1 = x*np.ones(len(self.ArrX)) - self.ArrX
                NewArr2 = self.ArrX[k]*np.ones(len(self.ArrX)) - self.ArrX
                NewArr2[k]=1
                NewArr1[k]=1
                P += np.prod(NewArr1)/np.prod(NewArr2)*self.ArrF[k]
            PL.append(P)
        return(PL)

