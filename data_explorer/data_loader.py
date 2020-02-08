import abc
from typing import Any, List, TypeVar

from column_type import Column


TDataLoader = TypeVar('TDataLoader', bound='DataLoader')


class DataLoader:
    @abc.abstractmethod
    def load(self: TDataLoader) -> bool:
        return False

    @abc.abstractmethod
    def get_headers(self) -> List[str]:
        return []

    @abc.abstractmethod
    def get_column_types(self) -> List[Column]:
        return []

    @abc.abstractmethod
    def get_data(self) -> List[List[Any]]:
        return []
