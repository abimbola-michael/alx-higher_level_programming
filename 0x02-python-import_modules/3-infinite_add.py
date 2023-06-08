#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_count = 0
    for i in range(len(sys.argv) - 1):
        total_count += int(sys.argv[i + 1])
    print("{}".format(total_count))
