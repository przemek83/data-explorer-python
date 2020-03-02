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
        print('%s completed in %.6fs' % (self.__name, end - self.__begin))
