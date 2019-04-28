import data_loader


class FileDataLoader(data_loader.DataLoader):
    def load(self, input_file):
        for line in input_file:
            print(line.rstrip("\n"))

        return True, []
