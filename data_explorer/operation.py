from typing import Dict, Tuple

from dataset import Dataset, Query


class Operation:
    def __init__(self, dataset: Dataset):
        self._dataset: Dataset = dataset

    def execute(self, query: Query) -> Dict[int, float]:
        pass

    def get_column_name_to_id(self, column_id: int) -> str:
        pass

    def get_column_id_to_name(self, column_name: str) -> Tuple[bool, int]:
        return self._dataset.get_column_id_from_name(column_name)
