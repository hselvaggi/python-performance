import numpy as np
import pandas as pd
import dask as ds
import dask.dataframe
from performance.utils import TimeFunction
from multiprocessing.pool import Pool
from collections import deque

""" Number of elements for the simple data transformation """
DATA_SIZE = 10000

""" Size for the DataFrames to be used on the join operation """
CITY_COUNT = 120
PEOPLE_COUNT = 10000
NUM_PARTITIONS=10
NUM_CORES=8


@TimeFunction
def calculate_on_dask():
    df = pd.DataFrame(np.random.randn(DATA_SIZE, 1), columns=['values'])
    df = ds.dataframe.from_pandas(df, 10)

    df.apply(axis=1, func=lambda x: x * x)

    df.compute()


@TimeFunction
def calculate_on_pandas():
    df = pd.DataFrame(np.random.randn(DATA_SIZE, 1), columns=['values'])

    df.apply(axis=1, func=lambda x: x * x)


def generate_person_table():
    names = ['Harold', 'Nahuel', 'Kirsten', 'Katherina']
    return [(i % CITY_COUNT, names[i % 4] + str(i)) for i in range(PEOPLE_COUNT)]


def generate_city_table():
    names = ['Montevideo', 'Canelones', 'Maldonado', 'Soriano', 'Minas', 'Rivera', 'Salto', 'Paysandu']
    return [(i % CITY_COUNT, names[i % 8] + str(i)) for i in range(CITY_COUNT)]


def parallelize_dataframe(df, func):
    df_split = np.array_split(df, NUM_PARTITIONS)
    pool = Pool(NUM_CORES)
    try:
        df = pd.concat(pool.map(func, df_split))
    finally:
        pool.close()
        pool.join()
    return df


@TimeFunction
def pandas_join():
    people = pd.DataFrame(generate_person_table(), columns=['city_id', 'names'])
    cities = pd.DataFrame(generate_city_table(), columns=['city_id', 'city'])

    result = people.merge(cities, on='city_id', how='left')


def merge_helper(df):
    return df.merge(cities, on='city_id', how='left')


@TimeFunction
def pandas_multiprocessing():
    global cities
    people = pd.DataFrame(generate_person_table(), columns=['city_id', 'names'])
    cities = pd.DataFrame(generate_city_table(), columns=['city_id', 'city'])

    parallelize_dataframe(people, merge_helper)

    cities = None

@TimeFunction
def dask_join():
    people = pd.DataFrame(generate_person_table(), columns=['city_id', 'names'])
    cities = pd.DataFrame(generate_city_table(), columns=['city_id', 'city'])

    people_dask = ds.dataframe.from_pandas(people,20)
    cities_dask = ds.dataframe.from_pandas(cities,20)

    result_dask = people_dask.merge(cities_dask, how='left', on='city_id').compute()


@TimeFunction
def dask_filter():
    people = pd.DataFrame(generate_person_table(), columns=['city_id', 'names'])
    people_dask = ds.dataframe.from_pandas(people, 10)

    people_dask[people_dask['city_id'] == 1].compute()


@TimeFunction
def pandas_filter():
    people = pd.DataFrame(generate_person_table(), columns=['city_id', 'names'])

    people[people['city_id'] == 1]


if __name__ == '__main__':
    for i in range(10):
        calculate_on_dask()
        calculate_on_pandas()
        pandas_join()
        dask_join()
        pandas_multiprocessing()
        dask_filter()
        pandas_filter()

    pandas_join.print_stats()
    dask_join.print_stats()
    calculate_on_dask.print_stats()
    calculate_on_pandas.print_stats()
    pandas_multiprocessing.print_stats()
    dask_filter.print_stats()
    pandas_filter.print_stats()