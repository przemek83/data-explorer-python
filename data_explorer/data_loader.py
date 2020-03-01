import abc
from typing import Any, List, TypeVar

from column_type import ColumnType


TDataLoader = TypeVar('TDataLoader', bound='DataLoader')


class DataLoader:
    @abc.abstractmethod
    def load(self: TDataLoader) -> bool:
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
