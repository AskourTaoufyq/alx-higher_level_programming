#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    order_keys = sorted(a_dictionary.keys())
    for key in order_keys:
        print("{}: {}".format(key, a_dictionary[key]))

