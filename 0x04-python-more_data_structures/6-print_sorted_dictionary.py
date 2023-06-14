#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    for key in sorted(a_dict.keys()):
        print("{:s}: {}".format(key, a_dict[key]))
