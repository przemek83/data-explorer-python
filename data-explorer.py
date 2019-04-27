import sys


def exit_with_help():
    sys.exit(-1)


def parse_args():
    if len(sys.argv) != 2:
        exit_with_help()

    return sys.argv[1]


def main():
    file = parse_args()
    print("data file: " + file)


main()
