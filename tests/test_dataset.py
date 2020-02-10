import io
from unittest.mock import patch

from column_type import Column
from dataset import Dataset
from file_data_loader import FileDataLoader


@patch('file_data_loader.FileDataLoader.load')
def test_load_failed(mock_load) -> None:
    mock_load.return_value = False
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    assert not dataset.initialize()


@patch('file_data_loader.FileDataLoader.load')
def test_load_succeed(mock_load) -> None:
    mock_load.return_value = True
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    assert dataset.initialize()


@patch('file_data_loader.FileDataLoader.load')
@patch('file_data_loader.FileDataLoader.get_headers')
@patch('file_data_loader.FileDataLoader.get_column_types')
@patch('file_data_loader.FileDataLoader.get_data')
def test_loaded_content(mock_get_data, mock_get_column_types, mock_get_headers, mock_load) -> None:
    mock_load.return_value = True
    headers = ['a', 'b', 'c']
    mock_get_headers.return_value = headers
    column_types = [Column.INTEGER, Column.INTEGER, Column.STRING]
    mock_get_column_types.return_value = column_types
    data = [['d', 'e', 'f']]
    mock_get_data.return_value = data
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    assert dataset.headers == headers
    assert dataset.column_types == column_types
    assert dataset.data == data


@patch('file_data_loader.FileDataLoader.load')
@patch('file_data_loader.FileDataLoader.get_headers')
def test_get_column_id_from_name(mock_get_headers, mock_load) -> None:
    mock_load.return_value = True
    headers = ['a', 'b', 'c']
    mock_get_headers.return_value = headers
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    for i in range(3):
        assert dataset.get_column_id_from_name(headers[i]) == i
