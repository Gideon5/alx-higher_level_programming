#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(my_list):
        try:
          print(my_list[i])
        except Exception as e:
            print("Error")

