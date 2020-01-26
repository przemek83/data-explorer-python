from ColumnType import Column, column_type_from_string


class TestColumnTypeFromString:
    def test_integer(self):
        column = column_type_from_string("integer")
        assert column is Column.INTEGER

    def test_string(self):
        column = column_type_from_string("string")
        assert column is Column.STRING

    def test_empty_string(self):
        column = column_type_from_string("")
        assert column is Column.UNKNOWN

    def test_incorrect_type(self):
        column = column_type_from_string("")
        assert column is Column.UNKNOWN
