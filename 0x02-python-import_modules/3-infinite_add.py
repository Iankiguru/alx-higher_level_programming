#!/usr/bin/python3
from sys import argv

j, resend = 1, 0

if __name__ == '__main__':
    while j < len(argv):
        resend += int(argv[j])
        j += 1
    print(resend)
