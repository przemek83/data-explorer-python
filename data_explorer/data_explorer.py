import argparse
import sys

from dataset import Dataset, OperationType, Query
from file_data_loader import FileDataLoader
from operation import Operation
from performance_checker import PerformanceChecker


def parse_args(args) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Small tool for aggregating and grouping data.')
    parser.add_argument('file', type=str, help='Input file')
    parser.add_argument('operation',
                        choices=[op.value for op in OperationType],
                        type=str.lower, help='Arythmetic operation to perform')
    parser.add_argument('aggregation', type=str, help='Aggregation column (numerical only)')
    parser.add_argument('grouping', type=str, help='Grouping by column')

    return parser.parse_args(args)


def load_data(file_name: str) -> Dataset:
    try:
        with open(file_name, 'r') as file:
            loader = FileDataLoader(file)
            dataset = Dataset(loader)
            dataset.initialize()
    except OSError:
        print('Cannot open ' + file_name + ' file, exiting.', file=sys.stderr)
        sys.exit(-1)
    return dataset


def main() -> None:
    args = parse_args(sys.argv[1:])

    with PerformanceChecker('Data loading'):
        dataset = load_data(args.file)

    operation = Operation(dataset)
    query = Query(OperationType(args.operation),
                  operation.column_name_to_id(args.aggregation)[1],
                  operation.column_name_to_id(args.grouping)[1])
    with PerformanceChecker('Operation'):
        results = operation.execute(query)

    print('Results: ', results)


if __name__ == '__main__':
    main()
