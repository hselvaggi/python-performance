from functools import lru_cache
from performance.utils import TimeFunction


@TimeFunction
def fibonacci(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@TimeFunction
@lru_cache(maxsize=1024)
def fibonacci_cache(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


@TimeFunction
def fibonacci_iterative(n):
    if n == 0:
        return 0
    if n < 3:
        return 1

    n_1 = 1
    n_2 = 1

    for n in range(3,n):
        temp = n_1 + n_2
        n_2 = n_1
        n_1 = temp

    return n_1 + n_2


if __name__ == '__main__':
    for times in range(100):
        for value in range(11):
            fibonacci(value)
            fibonacci_cache(value)
            fibonacci_iterative(value)

    fibonacci.print_stats()
    fibonacci_cache.print_stats()
    fibonacci_iterative.print_stats()