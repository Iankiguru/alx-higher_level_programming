#!/usr/bin/python3

import sys
if __name__ == "__main__":
 numb_args = len(sys.argv) - 1
 if numb_args == 0:
    print("0 arguments.")
 elif numb_args == 1:
    print("1 argument:")
 else:
    print("{} arguments:".format(numb_args))
 for j in range(numb_args):
     print("{}: {}".format(j + 1, sys.argv[j + 1]))
