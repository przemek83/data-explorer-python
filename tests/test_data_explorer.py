import argparse

from data_explorer.data_explorer import parse_args
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
                                    ['some_file.txt', '', 'other_score', 'other_movie_name']])
def test_parse_invalid_operation(params) -> None:
    try:
        parse_args(params)
        assert False
    except SystemExit:
        pass
