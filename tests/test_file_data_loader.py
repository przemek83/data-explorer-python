"""Tests for FileDataLoader class."""

import io

from column_type import ColumnType
from data import VALID_DATA_INPUT  # type: ignore
from file_data_loader import FileDataLoader
import pytest  # type: ignore


EMPTY_DATA_INPUT = ""

INPUT_WITH_WRONG_COLUMN_TYPE_NAME = """\
bla;bla;bla;bla
string;integer;bla;integer
tim;26;inception;8
"""

INPUT_WITH_WRONG_COLUMN_COUNT = """\
bla;bla;bla;bla
string;integer;integer
tim;26;inception;8
"""

INPUT_WITHOUT_DATA = """\
bla;bla;bla
string;integer;integer
"""


class TestFileDataLoader:
    @staticmethod
    def __get_loader(input_string: str) -> FileDataLoader:
        input_data = io.StringIO(input_string)
        return FileDataLoader(input_data)

    @pytest.mark.parametrize("input_string", [VALID_DATA_INPUT, INPUT_WITHOUT_DATA])
    def test_load_valid_file(self, input_string) -> None:
        loader = self.__get_loader(input_string)
        success = loader.load()
        assert success

    def test_headers_valid_file(self) -> None:
        loader = self.__get_loader(VALID_DATA_INPUT)
        loader.load()
        headers = loader.get_headers()
        assert headers == ["first_name", "age", "movie_name", "score"]

    def test_columns_valid_file(self) -> None:
        loader = self.__get_loader(VALID_DATA_INPUT)
        loader.load()
        columns = loader.get_column_types()
        assert columns == [
            ColumnType.STRING,
            ColumnType.INTEGER,
            ColumnType.STRING,
            ColumnType.INTEGER,
        ]

    def test_data_valid_file(self) -> None:
        loader = self.__get_loader(VALID_DATA_INPUT)
        loader.load()
        data = loader.get_data()
        assert data == [
            ["tim", "tim", "tamas", "tamas", "dave", "dave"],
            [26, 26, 44, 44, 0, 0],
            [
                "inception",
                "pulp_fiction",
                "inception",
                "pulp_fiction",
                "inception",
                "ender's_game",
            ],
            [8, 8, 7, 4, 8, 8],
        ]

    @pytest.mark.parametrize(
        "input_string",
        [
            EMPTY_DATA_INPUT,
            INPUT_WITH_WRONG_COLUMN_TYPE_NAME,
            INPUT_WITH_WRONG_COLUMN_COUNT,
        ],
    )
    def test_load_invalid_file(self, input_string: str) -> None:
        loader = self.__get_loader(input_string)
        success = loader.load()
        assert not success
