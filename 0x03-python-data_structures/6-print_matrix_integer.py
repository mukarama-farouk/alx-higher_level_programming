#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = [len(row) for row in matrix]
    for i in range(len(matrix)):
        for j in range(matrix_len[i]):
            if j != 0:
                print(" ", end=' ')

            print("{:d}".format(matrix[i][j]), end=" ")
        print()
