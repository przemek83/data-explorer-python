import argparse
from unittest.mock import mock_open, patch

from data import VALID_DATA_INPUT
from data_explorer.data_explorer import load_data, parse_args
import pytest  # type: ignore


@pytest.mark.parametrize('params', [['sample.txt', 'avg', 'score', 'movie_name'],
                                    ['some_file.txt', 'min', 'other_score', 'other_movie_name'],
                                    ['file.txt', 'max', 'other_score', 'other_movie_name']])
def test_parse_valid_args(params) -> None:
    args: argparse.Namespace = parse_args(params)
    assert args.file == params[0]
    assert args.operation == params[1]
    assert args.aggregation == params[2]
    assert args.grouping == params[3]


@pytest.mark.parametrize('params', [['sample.txt', 'bla', 'score', 'movie_name'],
                                    ['some_file.txt', '', 'other_score', 'other_movie_name'],
                                    ['some_file.txt', 'max', 'other_score']])
def test_parse_invalid_operation(params) -> None:
    try:
        parse_args(params)
        assert False
    except SystemExit:
        pass


@patch('builtins.open')
def test_load_data_invalid_file(mocked_open) -> None:
    mocked_open.side_effect = OSError
    try:
        load_data('')
        assert False
    except SystemExit:
        pass


@patch('builtins.open', new_callable=mock_open, read_data=VALID_DATA_INPUT)
@patch('dataset.Dataset.initialize')
def test_load_data_valid_file(dataset_initialize, _) -> None:
    load_data('')
    dataset_initialize.assert_called()
