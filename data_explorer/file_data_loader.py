from typing import Any, List, TextIO

from column_type import column_type_from_string, ColumnType
import data_loader


class FileDataLoader(data_loader.DataLoader):
    def __init__(self, input_file: TextIO):
        self.__input_file = input_file
        self.__headers: List[str] = []
        self.__column_types: List[ColumnType] = []
        self.__data: List[List[Any]] = []

    def load(self) -> bool:
        for line in self.__input_file:
            values = line.rstrip('\n').split(';')
            if not self.__headers:
                self.__headers = values
                continue
            if not self.__column_types:
                self.__load_column_types(values)
                continue
            try:
                self.__add_line_into_data(values)
            except ValueError:
                return False
        return self.__loaded_data_ok()

    def __add_line_into_data(self, data_values):
        for index, value in enumerate(data_values):
            if len(self.__data) <= index:
                self.__data.append([])
            if self.__column_types[index] == ColumnType.INTEGER:
                self.__data[index].append(int(value))
            else:
                self.__data[index].append(value)

    def get_headers(self) -> List[str]:
        return self.__headers

    def get_column_types(self) -> List[ColumnType]:
        return self.__column_types

    def get_data(self) -> List[List[Any]]:
        return self.__data

    def __load_column_types(self, column_strings: List[str]) -> None:
        for column_string in column_strings:
            self.__column_types.append(column_type_from_string(column_string))

    def __loaded_data_ok(self) -> bool:
        columns_valid = ColumnType.UNKNOWN not in self.__column_types
        return len(self.__headers) != 0 and len(self.__headers) == len(self.__column_types) and columns_valid
