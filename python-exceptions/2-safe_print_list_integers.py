#!/usr/bin/python3
def safe_print_list_integers(my_list=[], a=0):
    print_it = 0
    for i in range(a):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_it += 1
        except (TypeError, ValueError):
            continue
    print("")
    return print_it
