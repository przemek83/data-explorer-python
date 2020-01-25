import data_loader
from io import TextIOWrapper


class FileDataLoader(data_loader.DataLoader):
    def __init__(self, input_file: TextIOWrapper):
        self.input_file = input_file

    def load(self): 
        for line in self.input_file:
            print(line.rstrip("\n"))

        return True, []
