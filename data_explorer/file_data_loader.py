from typing import Any, List, TextIO

from column_type import column_type_from_string, ColumnType
import data_loader


class FileDataLoader(data_loader.DataLoader):
    def __init__(self, input_file: TextIO):
        self.input_file = input_file
        self.headers: List[str] = []
        self.column_types: List[ColumnType] = []
        self.data: List[List[Any]] = []

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

    def get_column_types(self) -> List[ColumnType]:
        return self.column_types

    def get_data(self) -> List[List[Any]]:
        return self.data

    def __load_column_types(self, column_strings: List[str]) -> None:
        for column_string in column_strings:
            self.column_types.append(column_type_from_string(column_string))

    def __loaded_data_ok(self) -> bool:
        columns_valid = ColumnType.UNKNOWN not in self.column_types
        equal_number_of_headers_and_column_types = len(self.headers) == len(self.column_types)
        return len(self.headers) != 0 and len(self.column_types) != 0 and \
            equal_number_of_headers_and_column_types and columns_valid
