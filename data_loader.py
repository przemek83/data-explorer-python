import abc


class DataLoader(object):
    @abc.abstractmethod
    def load(self):
        return False, []
