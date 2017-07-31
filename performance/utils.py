import time

class TimeFunction(object):
    def __init__(self, func):
        self.func = func
        self.all_time = 0
        self.calls = 0

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        self.all_time = self.all_time + time.time() - start
        self.calls = self.calls + 1
        return result

    def mean_call(self):
        return float(self.all_time) / float(self.calls)

    def num_calls(self):
        return self.calls

    def total_time(self):
        return self.all_time

    def print_stats(self):
        print('-' * 50)
        print('Stats for ' + str(self.func.__name__))
        print('Mean time: ' + str(self.mean_call()))
        print('Total time: ' + str(self.total_time()))
        print('Number of calls: ' + str(self.num_calls()))
        print('-' * 50)