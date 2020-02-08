from column_type import Column, column_type_from_string


def test_integer() -> None:
    column = column_type_from_string('integer')
    assert column is Column.INTEGER


def test_string() -> None:
    column = column_type_from_string('string')
    assert column is Column.STRING


def test_empty_string() -> None:
    column = column_type_from_string('')
    assert column is Column.UNKNOWN


def test_incorrect_type() -> None:
    column = column_type_from_string('')
    assert column is Column.UNKNOWN
