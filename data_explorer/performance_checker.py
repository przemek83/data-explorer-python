from timeit import default_timer as timer


class PerformanceChecker:
    def __init__(self, name):
        self.__name = name
        self.__begin = None

    def __enter__(self):
        self.__begin = timer()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        end = timer()
        print(f'{self.__name} completed in {end - self.__begin: .6f}')
