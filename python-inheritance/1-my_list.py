#!/usr/bin/python3
"""creating a clss to inherits form list"""

class MyList(list):
    """prints the list, but sorted"""

    def print_sorted(self):
        self.list = sorted(self)
        print(self.list)

