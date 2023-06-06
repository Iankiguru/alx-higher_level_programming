#!/usr/bin/python3
for s in range(0, 8):
    for m in range(s + 1, 10):
        print("{:d}{:d}".format(s, m), end=', ')
print("{:d}{:d}".format(s + 1, m))
