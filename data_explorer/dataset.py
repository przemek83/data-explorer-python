from dataclasses import dataclass
from enum import Enum
from typing import Any, List

from column_type import Column
from data_loader import DataLoader


class Operation(Enum):
    AVG = 'avg'
    MIN = 'min'
    MAX = 'max'


@dataclass
class Query:
    operation: Operation
    aggreagete_column_id: int
    grouping_coulm_id: int


class Dataset:
    def __init__(self, loader: DataLoader):
        self.loader: DataLoader = loader
        self.headers: List[str] = list()
        self.column_types: List[Column] = list()
        self.data: List[List[Any]] = list()

    def initialize(self) -> bool:
        if not self.loader.load():
            return False
        self.headers = self.loader.get_headers()
        self.column_types = self.loader.get_column_types()
        self.data = self.loader.get_data()
        return True

    def execute_query(self, query: Query) -> float:
        pass
