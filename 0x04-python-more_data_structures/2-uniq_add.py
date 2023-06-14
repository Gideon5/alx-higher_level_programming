#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_numbers = []
    for x in my_list:
        if x not in uniq_numbers:
            uniq_numbers.append(x)
    return sum(uniq_numbers)
