from tqdm import tqdm

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


