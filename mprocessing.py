from performance.utils import TimeFunction
from multiprocessing import Pool
from time import sleep


def chunks(L, n):
    for i in range(0, len(L), n):
        yield L[i:i+n]


def sum_range(big_range):
    sleep(10)
    return sum(big_range)


@TimeFunction
def inline_sum(big_range):
    return sum_range(big_range)


@TimeFunction
def parallel_sum(big_range):
    ranges = list(chunks(big_range, 500))

    pool = Pool(8)
    result = pool.map(sum_range, ranges)
    pool.close()
    pool.join()
    return sum(result)


if __name__ == '__main__':
    print(inline_sum(list(range(10000))))
    print(parallel_sum(list(range(10000))))

    inline_sum.print_stats()
    parallel_sum.print_stats()