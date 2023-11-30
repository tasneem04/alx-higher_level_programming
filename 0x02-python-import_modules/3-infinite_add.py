#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    argv = sys.argv
    argv_sum = 0
    for i in range(1, (argv_len)):
        argv_sum += int(argv[i])
    print("{}".format(argv_sum), end='\n')
