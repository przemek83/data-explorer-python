import abc


class DataLoader(object):
    @abc.abstractmethod
    def load(self, input_file):
        return False, []
