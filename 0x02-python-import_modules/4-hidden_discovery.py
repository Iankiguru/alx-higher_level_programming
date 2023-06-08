#!/usr/bin/python3
import hidden_4

j = 0

if __name__ == '__main__':
    my_list = dir(hidden_4)
    new_list = sorted(my_list)
    while j < len(new_list):
        if new_list[j][0] != '_':
            print(new_list[j])
        j += 1
