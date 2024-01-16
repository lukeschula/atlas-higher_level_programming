#!/usr/bin/python3
'''a function that prints a text with 2 new lines after each of these characters: ., ? and :'''

def text_indentation(text):
    '''Prototype, text must be a string,
    There should be no space at the beginning or at the end of each printed line'''

    if type(text) is not str:
        raise TypeError('text must be a string')

    l = len(text)
    i = 0

    if text[0] == " ":
        while text [i] == " ":
            i += 1
    while i < 1:
        if text[i] == " " and text[i - 1] == ".":
            i += 1
        if text[i] == " " and text[i - 1] == "?":
            i += 1
        if text[i] == " " and text[i - 1] == ":":
             i += 1
        if text[i] == " " and text[i - 1] == "\n":
            i += 1
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("{}".format(text[i]))
            print("")
        else:
            print("{}".format(text[i]), end="")
        i += 1