# filename : array.py

import random as rand

class Item(object) :
    def __init__(self, f : int, s : int) :
        self.first = f
        self.second = s

    def __str__(self) :
        return "{} : ({}, {})".format(self.__class__.__name__, self.first, self.second)

def main() :
    print(rand.randint(0, 100))
    return
    table = []
    for i in range(0, 16) :
        table.append(Item(i, i * (i - 1)))

    for tmp in table :
        print (tmp, end = "; ")
    print ()

    for tmp in table :
        if tmp.first == 8 :
            tmp.second = 8

    for tmp in table :
        print (tmp, end = "; ")
    print ()

    return

if __name__ == "__main__" :
    main()
