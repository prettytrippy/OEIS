import time
import numpy as np

"""
Calculate the nth Fibonacci number using the matrix multiplication method.
As it turns out,
| 1 1 | ^ n 
| 1 0 |  
gives us the nth Fibonacci number in its upper left corner. 
Instead of full matrix multiplcation, I diagonalize the matrix.
This way, raising it to the power of n is as simple as two matrix multiplications, and 2 * n * log_2(n) scalar multiplies
"""

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
    print(end-start)