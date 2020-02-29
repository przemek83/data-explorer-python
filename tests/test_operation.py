from unittest.mock import patch

from operation import Operation


@patch('dataset.Dataset.column_name_to_id')
@patch('dataset.Dataset')
def test_column_name_to_id(dataset, mock_dataset_column_name_to_id) -> None:
    mock_dataset_column_name_to_id.return_value = True, 1
    operation = Operation(dataset)
    assert (True, 1) == operation.column_name_to_id('something')
