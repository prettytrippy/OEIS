from tqdm import tqdm

"""
Brocard's conjecture:
The only pairs (m, n) satisfying this equation:
m^2 - 1 = n!
Are (5, 4), (11, 5), and (71, 7)
Computational searches have failed to find more, but the conjecture remains unproven.
"""

def is_fac(n):
    limit = n
    for i in range(1, limit):
        if ((n // i) * i) != n:
            return False
        n //= i
        if n == 1:
            return True
    return False

def is_brocard(m):
    return is_fac(m * m - 1)

answers = set()

for i in tqdm(range(1, 10000000)):
    if is_brocard(i):
        print(i)


