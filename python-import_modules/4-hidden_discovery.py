#!/usr/bin/python3

import hidden_4

def main():
    x = dir(hidden_4)
    for i in range(len(x)):
        if(x[i][0] != '_'):
            print("{}".format(x[i]))

    if  __name__ == "__main__":
        main()
