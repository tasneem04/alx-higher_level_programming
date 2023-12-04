#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if  matrix is None:
        print(' ')
    else:
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix)):
                print(" {:d}".format(matrix[row][col]), end='')
            print(end='\n')
