import math
import time
from pprint import pprint
import numpy as np

M = [
    [1, 1], 
    [1, 0]
]

root5 = np.sqrt(5)

lambda1 = (1 + root5) / 2
lambda2 = (1 - root5) / 2

P = np.array([
    [lambda1, 1],
    [lambda2, 1]
])

PI = np.array([
    [1/root5, -1/root5],
    [(root5-1)/(2*root5), (root5+1)/(2*root5)]
])

def fibonnaci(n):
    D = np.diag([
        np.power(lambda1, n), 
        np.power(lambda2, n)
    ])
    product = P@D@PI
    return np.round(product[0][0])
    
for i in range(1<<30):
    start = time.time()
    f = fibonnaci(i)
    end = time.time()
    if (end-start) > .999999:
        print(f"Failed at the {i}th Fibonacci number")
        break