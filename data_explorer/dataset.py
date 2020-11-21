from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Tuple

from column_type import ColumnType
from data_loader import DataLoader


class OperationType(Enum):
    AVG = 'avg'
    MIN = 'min'
    MAX = 'max'


@dataclass
class Query:
    operation_type: OperationType
    aggregate_column_id: int
    grouping_column_id: int


class Dataset:
    def __init__(self, loader: DataLoader):
        self.__loader: DataLoader = loader
        self.__headers: List[str] = list()
        self.__column_types: List[ColumnType] = list()
        self.__data: List[List[Any]] = list()

    def initialize(self) -> bool:
        if not self.__loader.load():
            return False
        self.__headers = self.__loader.get_headers()
        self.__column_types = self.__loader.get_column_types()
        self.__data = self.__loader.get_data()
        return True

    def column_name_to_id(self, name: str) -> Tuple[bool, int]:
        try:
            index = self.__headers.index(name)
            return True, index
        except ValueError:
            return False, len(self.__headers)

    def column_id_to_name(self, column_id: int) -> Tuple[bool, str]:
        try:
            name = self.__headers[column_id]
            return True, name
        except IndexError:
            return False, ''

    def get_column_type(self, column_id: int) -> Tuple[bool, ColumnType]:
        try:
            column = self.__column_types[column_id]
            return True, column
        except IndexError:
            return False, ColumnType.UNKNOWN

    def get_data(self, column_id: int) -> Tuple[bool, List[Any]]:
        try:
            data = self.__data[column_id]
            return True, data
        except IndexError:
            return False, list()
