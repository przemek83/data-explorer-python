from enum import Enum


class Column(Enum):
    INTEGER = "integer"
    STRING = "string"
    UNKNOWN = ""


def column_type_from_string(column_type_string: str) -> Column:
    for column in Column:
        if column.value == column_type_string:
            return column
    return Column.UNKNOWN
