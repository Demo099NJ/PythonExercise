# filename : list.py

class Tmp(object) :
    def __init__(self, val : int) :
        self.first = val
        self.second = val * 2

    def __str__(self) :
        return "({}, {})".format(self.first, self.second)

def test_list_append() :
    mylist = []
    for i in range(0, 16) :
        mylist.append(Tmp(i))
        i = 0

    print (mylist)

    tmp_list = []
    for tm in mylist :
        if tm.first == 6 :
            tmp_list.append(tm)
        tm = Tmp(100)

    print ("0x%x"%(id(mylist[6])))
    mylist.clear()
    print (mylist)
    mylist = tmp_list
    print (mylist)
    for temp in mylist :
        print (temp)
        print ("0x%x"%(id(temp)))

def main() :
    test_list_append()

main()
