from typing import Dict, Tuple

from dataset import Dataset, Query


class Operation:
    def __init__(self, dataset: Dataset):
        self.__dataset: Dataset = dataset

    def execute(self, query: Query) -> Dict[str, float]:
        pass

    def column_id_to_name(self, column_id: int) -> Tuple[bool, str]:
        return self.__dataset.column_id_to_name(column_id)

    def column_name_to_id(self, column_name: str) -> Tuple[bool, int]:
        return self.__dataset.column_name_to_id(column_name)
