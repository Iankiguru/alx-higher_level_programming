#!/usr/bin/python3
"""Defines a given peak-finding Algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak number in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    k = int(length / 2)
    list = list_of_integers

    if k - 1 < 0 and k + 1 >= length:
        return list[k]
    elif k - 1 < 0:
        return list[k] if list[k] > list[k + 1] else list[k + 1]
    elif k + 1 >= length:
        return list[k] if list[k] > list[k - 1] else list[k - 1]

    if list[k - 1] < list[k] > list[k + 1]:
        return list[k]

    if list[k + 1] > list[k - 1]:
        return find_peak(list[k:])
    return find_peak(list[:k])
