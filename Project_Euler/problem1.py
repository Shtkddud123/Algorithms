# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np

def multiple34(n):
    a = 0 
    for i in range(0,n):
        if i % 3 == 0:
            a += i
        elif i % 5 == 0:
            a += i
    return a 

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def even_fib(n):
    even_answer = 0
    j = 0
    array = np.arange(n)
    while j <= n:
        if even_answer <= 4000000:
            if (fib(j) % 2 == 0):
                even_answer += fib(j)
            print fib(j), even_answer             
        j += 1
                   

        
        
d = even_fib(1000)
print d 
