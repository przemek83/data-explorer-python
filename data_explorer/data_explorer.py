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
                        type=str.lower, help='Arithmetic operation to perform')
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


def get_column_id(operation: Operation, column_name: str) -> int:
    column_found, column_id = operation.column_name_to_id(column_name)
    if not column_found:
        print('Column ' + column_name + ' not found.', file=sys.stderr)
        sys.exit(-1)
    return column_id


def create_query(operation: Operation, args: argparse.Namespace) -> Query:
    aggregate_column_id = get_column_id(operation, args.aggregation)
    grouping_column_id = get_column_id(operation, args.grouping)
    operation_type = OperationType(args.operation)
    return Query(operation_type, aggregate_column_id, grouping_column_id)


def main() -> None:
    args = parse_args(sys.argv[1:])

    with PerformanceChecker('Data loading'):
        dataset = load_data(args.file)

    operation = Operation(dataset)
    query = create_query(operation, args)
    with PerformanceChecker('Operation'):
        results = operation.execute(query)

    print('Results: ', results)


if __name__ == '__main__':
    main()
