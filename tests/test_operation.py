import io
from typing import Dict
from unittest.mock import patch

from data import VALID_DATA_INPUT  # type: ignore
from dataset import Dataset, OperationType, Query
from file_data_loader import FileDataLoader
from operation import Operation
import pytest  # type: ignore


@patch("dataset.Dataset.column_name_to_id")
@patch("dataset.Dataset")
def test_column_name_to_id(dataset, mock_dataset_column_name_to_id) -> None:
    mock_dataset_column_name_to_id.return_value = True, 1
    operation = Operation(dataset)
    assert (True, 1) == operation.column_name_to_id("something")


@patch("dataset.Dataset.column_id_to_name")
@patch("dataset.Dataset")
def test_column_id_to_name(dataset, mock_dataset_column_id_to_name) -> None:
    mock_dataset_column_id_to_name.return_value = (True, "something")
    operation = Operation(dataset)
    assert (True, "something") == operation.column_id_to_name(1)


def prepare_operation() -> Operation:
    input_data = io.StringIO(VALID_DATA_INPUT)
    dataset = Dataset(FileDataLoader(input_data))
    dataset.initialize()
    return Operation(dataset)


def check_results(operation: Operation, query: Query, expected_results: Dict) -> None:
    result = operation.execute(query)
    assert result == expected_results


@pytest.mark.parametrize(
    "operation_type, aggreagete_column, grouping_column, expected_results",
    [
        (
            OperationType.MAX,
            "age",
            "movie_name",
            {"inception": 44, "pulp_fiction": 44, "ender's_game": 0},
        ),
        (
            OperationType.MAX,
            "score",
            "movie_name",
            {"inception": 8, "pulp_fiction": 8, "ender's_game": 8},
        ),
        (OperationType.MAX, "score", "first_name", {"tim": 8, "tamas": 7, "dave": 8}),
        (
            OperationType.MIN,
            "age",
            "movie_name",
            {"inception": 0, "pulp_fiction": 26, "ender's_game": 0},
        ),
        (
            OperationType.MIN,
            "score",
            "movie_name",
            {"inception": 7, "pulp_fiction": 4, "ender's_game": 8},
        ),
        (OperationType.MIN, "score", "first_name", {"tim": 8, "tamas": 4, "dave": 8}),
        (
            OperationType.AVG,
            "age",
            "movie_name",
            {"inception": 70 / 3, "pulp_fiction": 35, "ender's_game": 0},
        ),
        (
            OperationType.AVG,
            "score",
            "movie_name",
            {"inception": 7.666666666666667, "pulp_fiction": 6, "ender's_game": 8},
        ),
        (OperationType.AVG, "score", "first_name", {"tim": 8, "tamas": 5.5, "dave": 8}),
        (OperationType.AVG, "wrong", "first_name", {}),
        (OperationType.AVG, "score", "wrong", {}),
    ],
)
def test_operation(
    operation_type, aggreagete_column, grouping_column, expected_results
) -> None:
    operation = prepare_operation()
    query = Query(
        operation_type,
        operation.column_name_to_id(aggreagete_column)[1],
        operation.column_name_to_id(grouping_column)[1],
    )
    check_results(operation, query, expected_results)
