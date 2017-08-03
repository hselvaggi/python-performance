from performance.utils import TimeFunction
from collections import deque


@TimeFunction
def simple_loop(x):
    val = 0
    for i in range(x):
        val += i
    return val


@TimeFunction
def comprehenson_calc(x):
    return list([ i * i for i in range(x)])


@TimeFunction
def map_calc(x):
    return list(map(lambda a: a * a, range(x)))


@TimeFunction
def comprehension_dummy_data():
    names = ['Harold', 'Nahuel', 'Kirsten', 'Katherina']
    return [ (i, names[i % 3] + str(i)) for i in range(100)]


@TimeFunction
def deque_dummy_data():
    values = deque()
    names = ['Harold', 'Nahuel', 'Kirsten', 'Katherina']

    for i in range(200):
        values.append((i, names[i % 3]))


@TimeFunction
def list_dummy_data():
    values = []
    names = ['Harold', 'Nahuel', 'Kirsten', 'Katherina']

    for i in range(200):
        #values.append((i, names[i % 3]))
        values += (i, names[i % 3])

if __name__ == '__main__':

    for i in range(1000):
        map_calc(100)
        comprehenson_calc(100)

        comprehension_dummy_data()
        deque_dummy_data()
        list_dummy_data()

    map_calc.print_stats()
    comprehenson_calc.print_stats()

    comprehension_dummy_data.print_stats()
    deque_dummy_data.print_stats()
    list_dummy_data.print_stats()
