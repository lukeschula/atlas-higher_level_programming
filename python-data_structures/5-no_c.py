#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    idx_ctr = 0
    for index in new_str:
        if index == 'c' or index == 'C':
            new_str[idx_ctr] = ""
        idx_ctr += 1
        return "".join(new_str)
