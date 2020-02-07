from ColumnType import Column
import file_data_loader
import io
import pytest

valid_data_input = '''\
first_name;age;movie_name;score
string;integer;string;integer
tim;26;inception;8
tim;26;pulp_fiction;8
tamas;44;inception;7
tamas;44;pulp_fiction;4
dave;0;inception;8
dave;0;ender's_game;8
'''

empty_data_input = ""

input_with_wrong_column_name = '''\
bla;bla;bla;bla
string;integer;bla;integer
tim;26;inception;8
'''

input_with_wrong_column_count = '''\
bla;bla;bla;bla
string;integer;integer
tim;26;inception;8
'''

input_without_data = '''\
bla;bla;bla
string;integer;integer
'''


class TestFileDataLoader:
    @staticmethod
    def __get_loader(input_string) -> file_data_loader.FileDataLoader:
        input_data = io.StringIO(input_string)
        return file_data_loader.FileDataLoader(input_data)

    @pytest.mark.parametrize("input_string", [valid_data_input, input_without_data])
    def test_load_valid_file(self, input_string):
        loader = self.__get_loader(valid_data_input)
        ok = loader.load()
        assert ok

    def test_headers_valid_file(self):
        loader = self.__get_loader(valid_data_input)
        loader.load()
        headers = loader.get_headers()
        assert headers == ["first_name", "age", "movie_name", "score"]

    def test_columns_valid_file(self):
        loader = self.__get_loader(valid_data_input)
        loader.load()
        columns = loader.get_column_types()
        assert columns == [Column.STRING, Column.INTEGER, Column.STRING, Column.INTEGER]

    def test_data_valid_file(self):
        loader = self.__get_loader(valid_data_input)
        loader.load()
        data = loader.get_data()
        assert data == [['tim', '26', 'inception', '8'],
                        ['tim', '26', 'pulp_fiction', '8'],
                        ['tamas', '44', 'inception', '7'],
                        ['tamas', '44', 'pulp_fiction', '4'],
                        ['dave', '0', 'inception', '8'],
                        ['dave', '0', "ender's_game", '8']]

    @pytest.mark.parametrize("input_string",
                             [empty_data_input, input_with_wrong_column_name, input_with_wrong_column_count])
    def test_load_invalid_file(self, input_string):
        loader = self.__get_loader(input_string)
        ok = loader.load()
        assert not ok
