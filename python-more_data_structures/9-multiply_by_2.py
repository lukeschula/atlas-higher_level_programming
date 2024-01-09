#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {}
    for a, b in a_dictionary.items():
        new_dic[a] = b * 2
    return new_dic
