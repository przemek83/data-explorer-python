import abc
from typing import Any, List, TypeVar

from column_type import ColumnType


TypeDataLoader = TypeVar('TypeDataLoader', bound='DataLoader')


class DataLoader:
    @abc.abstractmethod
    def load(self: TypeDataLoader) -> bool:
        """abstract"""

    @abc.abstractmethod
    def get_headers(self) -> List[str]:
        """abstract"""

    @abc.abstractmethod
    def get_column_types(self) -> List[ColumnType]:
        """abstract"""

    @abc.abstractmethod
    def get_data(self) -> List[List[Any]]:
        """abstract"""
