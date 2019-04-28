import sys
from timeit import default_timer as timer


def exit_with_help():
    print("Usage: <binary> file", file=sys.stderr)
    print(" file - name of data file.", file=sys.stderr)
    sys.exit(-1)


def parse_args():
    if len(sys.argv) != 2:
        exit_with_help()

    return sys.argv[1]


def main():
    file_name = parse_args()

    begin = timer()
    try:
        with open(file_name, "r") as file:
            file.readable()
            for line in file:
                print(line.rstrip("\n"))
    except OSError:
        print("Cannot open " + file_name + " file, exiting.", file=sys.stderr)
        sys.exit(-1)

    print()
    end = timer()
    print("Data loaded in %.6fs" % (end-begin))


main()
