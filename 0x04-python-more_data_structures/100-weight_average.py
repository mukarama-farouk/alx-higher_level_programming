#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0

    for tup in my_list:
        total_score = total_score + (tup[0] * tup[1])

        total_weight = total_weight + tup[1]

    return (total_score / total_weight)
