"""
 The intention of this file is to show how different parameters on numba's jit decoration can affect
the performance of a function.
"""

from performance.utils import TimeFunction
from numba import jit, void


@TimeFunction
def simple_function():
    for i in range(100):
        [x * x for x in range(1000)]


@TimeFunction
@jit
def simple_function_numba():
    for i in range(100):
        [x * x for x in range(1000)]


@TimeFunction
@jit(void())
def simple_function_numba_optimized():
    for i in range(100):
        [x * x for x in range(1000)]


if __name__ == '__main__':
    result = simple_function()
    simple_function.print_stats()

    result = simple_function_numba()
    simple_function_numba.print_stats()

    result = simple_function_numba_optimized()
    simple_function_numba_optimized.print_stats()