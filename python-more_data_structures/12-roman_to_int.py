#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) != str:
        return 0
    else:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                      'M': 1000}
        roman_lst = list(roman_string)
        roman_num = 0
        for x in range(len(roman_lst)):
            if x == 0:
                roman_num += roman_dict[roman_lst[x]]
            elif roman_dict[roman_lst[x]] > roman_dict[roman_lst[x - 1]]:
                roman_num += roman_dict[roman_lst[x]] - \
                            2 * roman_dict[roman_lst[x - 1]]
            else:
                roman_num += roman_dict[roman_lst[x]]
        return roman_num
