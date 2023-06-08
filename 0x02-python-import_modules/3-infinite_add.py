#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    int_args = sys.argv[1:]

    args_len = len(int_args)

    if args_len == 0:
        print("0")
    else:
        add = 0
        for arg in int_args:
            add = add + int(arg)
        print(add)
