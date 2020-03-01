import io
from unittest.mock import patch

from column_type import ColumnType
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
    column_types = [ColumnType.INTEGER, ColumnType.INTEGER, ColumnType.STRING]
    mock_get_column_types.return_value = column_types
    data = [['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]
    mock_get_data.return_value = data
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    for i, header in enumerate(headers, 0):
        assert dataset.column_id_to_name(i) == (True, header)
    for i, column_type in enumerate(column_types, 0):
        assert dataset.get_column_type(i) == (True, column_type)
    for i, data_column in enumerate(data, 0):
        assert dataset.get_data(i) == (True, data_column)


@patch('file_data_loader.FileDataLoader.load')
@patch('file_data_loader.FileDataLoader.get_headers')
def test_column_name_to_id(mock_get_headers, mock_load) -> None:
    mock_load.return_value = True
    headers = ['a', 'b', 'c']
    mock_get_headers.return_value = headers
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    for i in range(3):
        assert dataset.column_name_to_id(headers[i]) == (True, i)
    assert dataset.column_name_to_id('d')[0] is False


@patch('file_data_loader.FileDataLoader.load')
@patch('file_data_loader.FileDataLoader.get_headers')
def test_column_id_to_name(mock_get_headers, mock_load) -> None:
    mock_load.return_value = True
    headers = ['a', 'b', 'c']
    mock_get_headers.return_value = headers
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    for i in range(3):
        assert dataset.column_id_to_name(i) == (True, headers[i])
    assert dataset.column_id_to_name(3)[0] is False


@patch('file_data_loader.FileDataLoader.load')
@patch('file_data_loader.FileDataLoader.get_column_types')
def test_get_column_type(mock_get_column_types, mock_load) -> None:
    mock_load.return_value = True
    columns = [ColumnType.INTEGER, ColumnType.INTEGER, ColumnType.STRING]
    mock_get_column_types.return_value = columns
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    for i in range(3):
        assert dataset.get_column_type(i) == (True, columns[i])
    assert dataset.get_column_type(3) == (False, ColumnType.UNKNOWN)


@patch('file_data_loader.FileDataLoader.load')
@patch('file_data_loader.FileDataLoader.get_data')
def test_get_data(mock_get_data, mock_load) -> None:
    mock_load.return_value = True
    data = [['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]
    mock_get_data.return_value = data
    dataset = Dataset(FileDataLoader(io.StringIO('')))
    dataset.initialize()
    for i in range(3):
        assert dataset.get_data(i) == (True, data[i])
    assert dataset.get_data(3)[0] is False
