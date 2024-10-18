"""Module containing column type related parts."""

from enum import Enum


class ColumnType(Enum):
    """Enum class containing supported column types."""

    INTEGER = "integer"
    STRING = "string"
    UNKNOWN = ""


def column_type_from_string(column_type_string: str) -> ColumnType:
    for column_type in ColumnType:
        if column_type.value == column_type_string:
            return column_type
    return ColumnType.UNKNOWN
