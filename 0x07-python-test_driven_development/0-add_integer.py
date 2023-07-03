#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b

