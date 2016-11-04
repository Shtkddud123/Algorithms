import numpy a np
import random

class buffon_needle():
    """ Calculation of pi through the Buffon's needle method"""
        def __init__(self,N,b):
            self.N = N
            self.b = b
        def direct_needle():
            self.Nhits = 0
            for i in np.nditer(N):
                x_center = np.random.uniform(0,self.b/2,self.N)
                theta = np.random.uniform(0,np.pi/2,self.N)
                x_tip = x_center - (a/2)*np.cos(theta) 

            if x_tip < 0:
                self.Nhits = = self.Nhits + 1

            return Nhits

        def direct_needle_II():
            x_center = np.random.uniform(0,self.b/2,self.N)
            x = np.random.uniform(0, 1, self.N)
            y = np.random.uniform(0, 1, self.N)
            THETA = np.sqrt(x**2 + y**2)

            if THETA > 1:
                x = np.random.uniform(0, 1, self.N)
                y = np.random.uniform(0, 1, self.N)
            
            x_tip  = x_center - (a/2)*(x/THETA)
            self.Nhits = 0
            
            if x_tip < 0:
                Nhits = 1

            return Nhits 

        
