#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return None
    else:
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix)):
                print(" {:d}".format(matrix[row][col]), end='')
            
            print(end='\n')

