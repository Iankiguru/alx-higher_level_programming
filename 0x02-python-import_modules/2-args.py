#!/usr/bin/python3
from sys import argv
j = 1

if __name__ == '__main__':
    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print('1 argument:')
        print('1: {}'.format(argv[1]))
    else:
        print('{:d} arguments:'.format(len(argv) - 1))
        while j < len(argv):
            print('{:d}: {:s}'.format(j, argv[j]))
            j += 1
