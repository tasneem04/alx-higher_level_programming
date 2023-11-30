#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv) - 1
    if argv == 0:
        print("{} arguments.".format(argv), end='\n')
    else:
        print("{} argument:".format(argv), end='\n')
        for i in range(1, (argv + 1)):
            print("{}: {}".format(i, sys.argv[i]), end='\n')
