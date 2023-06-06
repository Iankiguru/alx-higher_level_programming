#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if ord(word) >= 97 and ord(word) <= 122:
            word = chr(ord(word) - 32)
        print("{:s}".format(word), end='')

    print('\n', end="")
