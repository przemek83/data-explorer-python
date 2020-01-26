import data_loader
from typing import TextIO, List

from ColumnType import Column


class FileDataLoader(data_loader.DataLoader):
    def __init__(self, input_file: TextIO):
        self.input_file = input_file

    def load(self): 
        for line in self.input_file:
            print(line.rstrip("\n"))

        return True, []

    def get_headers(self) -> List[str]:
        pass

    def get_column_types(self) -> List[Column]:
        pass

    def get_data(self) -> List[List]:
        pass
