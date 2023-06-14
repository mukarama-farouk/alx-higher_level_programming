#!/usr/bin/python3
def number_keys(a_dictionary):
    n_keys = 0
    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        n_keys = n_keys + 1
    return(n_keys)
