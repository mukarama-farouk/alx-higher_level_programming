#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0

    try:
        for i in my_list[:x]:
            print(i, end='')
            num += 1
    except IndexError:
        pass
    finally:
        print()
        return num
