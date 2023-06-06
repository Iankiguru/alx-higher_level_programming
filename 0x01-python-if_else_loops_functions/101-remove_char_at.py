#!/usr/bin/python3
def remove_char_at(str, n):
    list1 = list(str)
    for j in range(n, len(list1)):
        if j == n:
            del list1[j]
    return ''.join(list1)

