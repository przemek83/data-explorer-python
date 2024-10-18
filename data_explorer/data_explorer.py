"""Main entry point of data explorer application."""

import sys

from operation import Operation
from performance_checker import PerformanceChecker
from utils import create_query, load_data, parse_args


def main() -> None:
    args = parse_args(sys.argv[1:])

    with PerformanceChecker("Data loading"):
        dataset = load_data(args.file)

    operation = Operation(dataset)
    query = create_query(operation, args)
    with PerformanceChecker("Operation"):
        results = operation.execute(query)

    print("Results: ", results)


if __name__ == "__main__":
    main()
