#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        return max(a_dictionary.items(), key=lambda x: x[1])[0]
