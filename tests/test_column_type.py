"""Module covering tests of logic from ColumnType."""

from column_type import column_type_from_string, ColumnType


def test_integer() -> None:
    column = column_type_from_string("integer")
    assert column is ColumnType.INTEGER


def test_string() -> None:
    column = column_type_from_string("string")
    assert column is ColumnType.STRING


def test_empty_string() -> None:
    column = column_type_from_string("")
    assert column is ColumnType.UNKNOWN


def test_incorrect_type() -> None:
    column = column_type_from_string("bla")
    assert column is ColumnType.UNKNOWN
