from ColumnType import Column, column_type_from_string
import file_data_loader
import io

sample_data_input = '''
first_name;age;movie_name;score
string;integer;string;integer
tim;26;inception;8
tim;26;pulp_fiction;8
tamas;44;inception;7
tamas;44;pulp_fiction;4
dave;0;inception;8
dave;0;ender's_game;8
'''


class TestFileDataLoader:
    @staticmethod
    def __get_loader() -> file_data_loader.FileDataLoader:
        input_data = io.StringIO()
        input_data.write(sample_data_input)
        return file_data_loader.FileDataLoader(input_data)

    def test_load_valid_file(self):
        loader = self.__get_loader()
        ok = loader.load()
        assert ok

    def test_headers_valid_file(self):
        loader = self.__get_loader()
        loader.load()
        headers = loader.get_headers()
        assert headers == ["first_name", "age", "movie_name", "score"]

    def test_columns_valid_file(self):
        loader = self.__get_loader()
        loader.load()
        columns = loader.get_column_types()
        assert columns == [Column.STRING, Column.INTEGER, Column.STRING, Column.INTEGER]

    def test_data_valid_file(self):
        loader = self.__get_loader()
        loader.load()
        data = loader.get_data()
        assert data == [["tim", "tim", "tamas", "tamas", "dave", "dave"],
                        [26, 26, 44, 44, 0, 0],
                        ["inception", "pulp_fiction", "inception", "pulp_fiction", "inception", "ender's_game"],
                        [8, 8, 7, 4, 8, 8]]
