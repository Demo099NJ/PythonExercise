# filename: test.py
import time
import random

def generate_continuous_array(begin : int, end : int) :
    haha = []

    for i in range(begin, end + 1) :
        haha.append(i)

    return haha

def generate_random_array(length : int, begin : int, end : int) :
    lala = []

    if begin > end :
        begin, end = end, begin

    for i in range(0, length) :
        lala.append(random.randint(begin, end))

    return lala

def test_remove() :
    haha = generate_continuous_array(0, 16)
    print (haha)

    lala = generate_random_array(10, 0, 15)
    print (lala)

    for tmp in haha :
        if tmp in lala :
            haha.remove(tmp)

    print (haha)

def control_pop() :
    tmp_list = generate_continuous_array(0, 16)
    print (tmp_list)

    tmp_random = generate_random_array(10, 0, 15)
    print (tmp_random)

    count = 0
    while count < len(tmp_list) :
        if tmp_list[count] in tmp_random :
            tmp_list.pop(count)
        else :
            count += 1

    print (tmp_list)

def another_way() :
    tmp_list = generate_continuous_array(0, 16)
    print (tmp_list)

    tmp_random = generate_random_array(10, 0, 15)
    print (tmp_random)

    tmp = []
    for i in tmp_list :
        if not i in tmp_random :
            tmp.append(i)

    tmp_list = tmp
    print (tmp_list)

def main() :
    test_remove()

    control_pop()

    another_way()

main()
