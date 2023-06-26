#!/usr/bin/python3
def raise_exception():
    x = "hello"
    if not isinstance(x, (int, float)):
        raise TypeError("Only integers and floats are allowed")
