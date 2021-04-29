#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    args = len(argv)
    sum = 0
    if args >= 2:
        for i in range(args - 1):
            sum = sum + int(argv[i + 1])
    print("{}".format(sum))
