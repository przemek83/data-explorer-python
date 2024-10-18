import argparse
from unittest.mock import mock_open, patch

from data import VALID_DATA_INPUT  # type: ignore
from utils import create_query, get_column_id, load_data, parse_args
from operation import Operation, OperationType
import pytest  # type: ignore


@pytest.mark.parametrize(
    "params",
    [
        ["sample.txt", "avg", "score", "movie_name"],
        ["some_file.txt", "min", "other_score", "other_movie_name"],
        ["file.txt", "max", "other_score", "other_movie_name"],
    ],
)
def test_parse_valid_args(params) -> None:
    args: argparse.Namespace = parse_args(params)
    assert args.file == params[0]
    assert args.operation == params[1]
    assert args.aggregation == params[2]
    assert args.grouping == params[3]


@pytest.mark.parametrize(
    "params",
    [
        ["sample.txt", "bla", "score", "movie_name"],
        ["some_file.txt", "", "other_score", "other_movie_name"],
        ["some_file.txt", "max", "other_score"],
    ],
)
def test_parse_invalid_operation(params) -> None:
    try:
        parse_args(params)
        assert False
    except SystemExit:
        pass


@patch("builtins.open")
def test_load_data_invalid_file(mocked_open) -> None:
    mocked_open.side_effect = OSError
    try:
        load_data("")
        assert False
    except SystemExit:
        pass


@patch("builtins.open", new_callable=mock_open, read_data=VALID_DATA_INPUT)
@patch("dataset.Dataset.initialize")
def test_load_data_valid_file(dataset_initialize, _) -> None:
    load_data("")
    dataset_initialize.assert_called()


@pytest.mark.parametrize("column_name_to_id_return_value", [(False, 4)])
@patch("operation.Operation.column_name_to_id")
@patch("dataset.Dataset")
def test_get_column_id_invalid_column(
    mock_dataset, mock_column_name_to_id, column_name_to_id_return_value
) -> None:
    mock_column_name_to_id.return_value = column_name_to_id_return_value
    try:
        get_column_id(Operation(mock_dataset), "column1")
        assert False
    except SystemExit:
        pass


@patch("operation.Operation.column_name_to_id")
@patch("dataset.Dataset")
def test_create_query(mock_dataset, mock_column_name_to_id) -> None:
    expected_aggreagete_column_id = 3
    expected_grouping_column_id = 4
    mock_column_name_to_id.side_effect = [
        (True, expected_aggreagete_column_id),
        (True, expected_grouping_column_id),
    ]
    args = argparse.Namespace()
    args.operation = "min"
    args.aggregation = "column1"
    args.grouping = "column2"
    query = create_query(Operation(mock_dataset), args)
    assert query.operation_type == OperationType.MIN
    assert query.aggregate_column_id == expected_aggreagete_column_id
    assert query.grouping_column_id == expected_grouping_column_id
