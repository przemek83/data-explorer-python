import argparse
import sys
from timeit import default_timer as timer

from dataset import Dataset, Operation
from file_data_loader import FileDataLoader


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Small tool for aggregating and grouping data.')
    parser.add_argument('file', type=str, help='Input file')
    parser.add_argument('operation',
                        choices=[op.value for op in Operation],
                        type=str.lower, help='Arythmetic operation to perform')
    parser.add_argument('aggregation', type=str, help='Aggregation column (numerical only)')
    parser.add_argument('grouping', type=str, help='Grouping by column')

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    begin = timer()
    try:
        with open(args.file, 'r') as file:
            loader = FileDataLoader(file)
            dataset = Dataset(loader)
            success = dataset.initialize()
            if success:
                print('Data loaded, action: <%s> <%s> grouped by <%s>' %
                      (args.operation, args.aggregation, args.grouping))

    except OSError:
        print('Cannot open ' + args.file + ' file, exiting.', file=sys.stderr)
        sys.exit(-1)

    print()
    end = timer()
    print('Data loaded in %.6fs' % (end - begin))


main()
