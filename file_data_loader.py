import data_loader
from typing import TextIO, List

from ColumnType import Column, column_type_from_string


class FileDataLoader(data_loader.DataLoader):
    def __init__(self, input_file: TextIO):
        self.input_file = input_file
        self.headers = []
        self.column_types = []
        self.data = []

    def load(self) -> bool:
        for line in self.input_file:
            line = line.rstrip('\n')
            if not self.headers:
                self.headers = line.split(';')
                continue
            if not self.column_types:
                self.__load_column_types(line.split(';'))
                continue
            self.data.append(line.rstrip('\n').split(';'))

        return self.__loaded_data_ok()

    def get_headers(self) -> List[str]:
        return self.headers

    def get_column_types(self) -> List[Column]:
        return self.column_types

    def get_data(self) -> List[List]:
        return self.data

    def __load_column_types(self, column_strings: List[str]) -> None:
        for column_string in column_strings:
            self.column_types.append(column_type_from_string(column_string))

    def __loaded_data_ok(self) -> bool:
        columns_valid = Column.UNKNOWN not in self.column_types
        equal_number_of_headers_and_column_types = len(self.headers) == len(self.column_types)
        return self.headers and self.column_types and equal_number_of_headers_and_column_types and columns_valid
