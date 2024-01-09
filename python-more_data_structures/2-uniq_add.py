#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = [el for el in my_list]
    return sum(set(new_list))
