#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_it = 0
    for it in range(x):
        try:
            print("{:d}".format(my_list[it]), end="")
            print_it += 1
        except IndexError:
            break
    print("")
    return print_it
