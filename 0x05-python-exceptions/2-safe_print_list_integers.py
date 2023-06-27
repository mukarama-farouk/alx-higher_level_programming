#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0

    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end='')
        except ValueError:
            pass
        except TypeError:
            pass
        else:
            num += 1

    print()
    return num
