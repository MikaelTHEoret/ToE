from math import gcd

def is_positional_composite(n):
    if n % 10 == 5:
        return True, 5
    for k in (3, 7, 9):
        nk = n * k
        A, d = nk // 10, nk % 10
        if d > 1 and A % d == 0:
            q = A // d
            if q > 1 and (gcd(d, k) == 1 or d == k):
                return True, d
    return False, None