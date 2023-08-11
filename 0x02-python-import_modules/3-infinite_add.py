#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    if count == 0:
        print("{}".format(count))
    else:
        total = 0
        for i in range(count):
            total += int(argv[i + 1])
        print("{}".format(total))
