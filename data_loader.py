import abc
from typing import Tuple, List
from ColumnType import Column


class DataLoader(object):
    @abc.abstractmethod
    def load(self) -> bool:
        return False

    @abc.abstractmethod
    def get_headers(self) -> List[str]:
        return []

    @abc.abstractmethod
    def get_column_types(self) -> List[Column]:
        return []

    @abc.abstractmethod
    def get_data(self) -> List[List]:
        return []
