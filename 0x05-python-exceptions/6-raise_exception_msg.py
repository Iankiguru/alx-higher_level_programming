#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not message:
        message = "Name exception occurred"
    raise NameError(message)
