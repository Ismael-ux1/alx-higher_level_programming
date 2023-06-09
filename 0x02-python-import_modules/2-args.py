#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv) - 1
if argc == 0:
    print(argc, "argument:")
else:
    print(argc, "arguments:")
    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
