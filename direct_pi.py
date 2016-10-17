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
        for i in range(0,self.N):
            print i 
            x = random.uniform(-1.0,1.0)
            y = random.uniform(-1.0,1.0)
            if ((x**2) + (y**2)) < 1:
                self.Nhits = self.Nhits + 1   
                       


