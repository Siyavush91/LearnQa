def calculate(s, m):
    return s + m


def create_tuple(x):
    i = tuple(range(x))
    return i


def factorial(num):
    fact = 1
    i = 2
    while i <= num:
        fact *= i
        i += 1
    return fact


def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
