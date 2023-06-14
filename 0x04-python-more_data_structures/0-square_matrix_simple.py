#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mult_matrix = [[x*x for x in y] for y in matrix]
    return mult_matrix


if __name__ == "__main__":
    square_matrix_simple()
