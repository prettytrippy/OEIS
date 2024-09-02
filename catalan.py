
def catalan(n):
    # Generate the nth Catalan number as fast as we can
    # (2n)! / ((n + 1)! * n)
    # I calculate 2n * 2n-1 * 2n-2 ... * n + 1, effectively dividing the n! factor out
    # In the same loop, calculate (n + 1)!, then return the quotient of the two numbers
    numerator = 1
    denominator = 1
    for i in range(1, n):
        numerator *= i + n + 1
        denominator *= i + 1
    return numerator // denominator

def catalan_generator():
    # It's faster to use recurrence relations to generate Catalan numbers iteratively
    numerator = 1
    denominator = 1
    yield numerator
    n = 1
    while True:
        # To get (2n)! from the (n - 1)th numerator, multiply by 2n * 2n-1
        numerator *= (2 * n) * (2 * n - 1)
        # Divide out the n + 1, effectively dividing by (n + 1)!
        numerator //= n + 1
        # Multiply the denominator by n, to take it from (n - 1)! to n!
        denominator *= n
        yield numerator // denominator
        n += 1