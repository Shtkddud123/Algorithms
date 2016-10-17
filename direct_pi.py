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
                
    def markov_pi(self,x_markov,y_markov,delta):
        """Pi comes out as four times the ratio of hits
        to trials 
        """
        self.x_markov = x_markov
        self.y_markov = y_markov
        self.delta = delta

        deltax = np.random.uniform(-self.delta, self.delta, self.N)
        deltay = np.random.uniform(-self.delta, self.delta, self.N)

        for i,j in np.nditer([deltax,deltay]):            
            if np.absolute(self.x_markov + i) < 1 and np.absolute(self.y_markov + j) < 1:

                self.x_markov = self.x_markov + i
                self.y_markov = self.y_markov + j                

                if (self.x_markov * self.x_markov) + (self.y_markov * self.y_markov) < 1:
                    self.Nhits = self.Nhits + 1 
