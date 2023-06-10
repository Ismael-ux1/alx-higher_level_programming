#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argz = len(sys.argv) - 1
    if (argz == 0):
        print(argz, "arguments.")
    elif (argz == 1):
        print(argz, "argument:".format(sys.argv[0]))
        print("1:", sys.argv[1])
    else:
        print(argz, "arguments:")
        for i in range(1, argz + 1):
            print("{}: {}".format(i, sys.argv[i]))
