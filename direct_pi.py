import numpy as np
import random

class SM_alg():
    """ 
    Calculate pi using direct sampling monte carlo algorithms
    """
    def __init__(self,N):
        self.N = N
        self.Nhits = 0
    def direct_sampling(self):

        x = np.random.uniform(-1, 1, self.N)
        y = np.random.uniform(-1, 1, self.N)

        for i,j in np.nditer([x,y]):
            if (i*i) + (j*j) < 1:
                self.Nhits = self.Nhits + 1
                
a = SM_alg(4000)
a.direct_sampling()
print a.Nhits 
