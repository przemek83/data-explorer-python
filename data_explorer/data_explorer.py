import argparse
import sys
from timeit import default_timer as timer

import file_data_loader


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Small tool for aggregating and grouping data.')
    parser.add_argument('file', type=str, help='Input file')
    parser.add_argument('operation',
                        choices=['avg', 'min', 'max'],
                        type=str, help='Arythmetic operation to perform')
    parser.add_argument('aggregation', type=str, help='Aggregation column (numerical only)')
    parser.add_argument('grouping', type=str, help='Grouping by column')

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    begin = timer()
    try:
        with open(args.file, 'r') as file:
            loader = file_data_loader.FileDataLoader(file)
            success = loader.load()
            headers = loader.get_headers()

            if success:
                print('Data loaded, headers count %d:, action: <%s> <%s> grouped by <%s>' %
                      (len(headers), args.operation, args.aggregation, args.grouping))

    except OSError:
        print('Cannot open ' + args.file + ' file, exiting.', file=sys.stderr)
        sys.exit(-1)

    print()
    end = timer()
    print('Data loaded in %.6fs' % (end - begin))


main()
