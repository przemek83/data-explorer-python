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
    aggreagete_column_id: int
    grouping_coulm_id: int


class Dataset:
    def __init__(self, loader: DataLoader):
        self._loader: DataLoader = loader
        self._headers: List[str] = list()
        self._column_types: List[ColumnType] = list()
        self._data: List[List[Any]] = list()

    def initialize(self) -> bool:
        if not self._loader.load():
            return False
        self._headers = self._loader.get_headers()
        self._column_types = self._loader.get_column_types()
        self._data = self._loader.get_data()
        return True

    def column_name_to_id(self, name: str) -> Tuple[bool, int]:
        try:
            index = self._headers.index(name)
            return True, index
        except ValueError:
            return False, -1

    def column_id_to_name(self, column_id: int) -> Tuple[bool, str]:
        try:
            name = self._headers[column_id]
            return True, name
        except IndexError:
            return False, ''

    def get_column_type(self, column_id: int) -> Tuple[bool, ColumnType]:
        try:
            column = self._column_types[column_id]
            return True, column
        except IndexError:
            return False, ColumnType.UNKNOWN

    def get_data(self, column_id: int) -> Tuple[bool, List[Any]]:
        try:
            data = self._data[column_id]
            return True, data
        except IndexError:
            return False, list()
