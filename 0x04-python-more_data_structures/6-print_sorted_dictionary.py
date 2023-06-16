#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        value = a_dictionary[key]
        print(key, value)
