from typing import Dict, Tuple

from dataset import Dataset, OperationType, Query


class Operation:
    def __init__(self, dataset: Dataset):
        self.__dataset: Dataset = dataset

    def execute(self, query: Query) -> Dict[str, float]:
        data_ok, aggregation_data = self.__dataset.get_data(query.aggregate_column_id)
        if not data_ok:
            return {}
        data_ok, grouping_data = self.__dataset.get_data(query.grouping_column_id)
        if not data_ok:
            return {}

        results: Dict[str, float] = {}
        if query.operation_type is OperationType.MIN:
            results = Operation.__compute_min(aggregation_data, grouping_data)
        if query.operation_type is OperationType.MAX:
            results = Operation.__compute_max(aggregation_data, grouping_data)
        if query.operation_type is OperationType.AVG:
            results = Operation.__compute_avg(aggregation_data, grouping_data)
        return results

    def column_id_to_name(self, column_id: int) -> Tuple[bool, str]:
        return self.__dataset.column_id_to_name(column_id)

    def column_name_to_id(self, column_name: str) -> Tuple[bool, int]:
        return self.__dataset.column_name_to_id(column_name)

    @staticmethod
    def __compute_min(aggregation_data, grouping_data) -> Dict[str, float]:
        return Operation.__compute_extreme(aggregation_data, grouping_data, lambda a, b: a > b)

    @staticmethod
    def __compute_max(aggregation_data, grouping_data) -> Dict[str, float]:
        return Operation.__compute_extreme(aggregation_data, grouping_data, lambda a, b: a < b)

    @staticmethod
    def __compute_extreme(aggregation_data, grouping_data, func) -> Dict[str, float]:
        results: Dict[str, float] = {}
        for index, aggregation in enumerate(aggregation_data):
            grouping = grouping_data[index]
            if grouping in results:
                if func(results[grouping], aggregation):
                    results[grouping] = aggregation
            else:
                results[grouping] = aggregation
        return results

    @staticmethod
    def __compute_avg(aggregation_data, grouping_data) -> Dict[str, float]:
        entries_sum: Dict[str, Tuple[int, int]] = Operation.__sum_entries(aggregation_data, grouping_data)
        results: Dict[str, float] = {}
        for _, (grouping, (calculated_count, calculated__sum)) in enumerate(entries_sum.items()):
            results[grouping] = calculated__sum / calculated_count
        return results

    @staticmethod
    def __sum_entries(aggregation_data, grouping_data) -> Dict[str, Tuple[int, int]]:
        results: Dict[str, Tuple[int, int]] = {}
        for index, grouping in enumerate(grouping_data):
            if grouping in results:
                current_values = results[grouping]
                results[grouping] = (current_values[0] + 1, current_values[1] + aggregation_data[index])
            else:
                results[grouping] = (1, aggregation_data[index])
        return results
