#!/usr/bin/python3
"""
Module to divide all elements of matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    Args:
        matrix(list of lists of integers or floats): to be divided matrix
        div(int/float): the number that divides the matrix
    Raises:
        TypeError:  -if matrix is not a list of integers/floats
                    -Each row of the matrix must have the same size
                    -if div is not of type int or float
        ZeroDivisionError: when div equal to 0
    Returns:
        new matrix
    """
    if not isinstance(matrix, (list, int, float)):
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    a = len(matrix[0])
    for i in matrix:
        if a != len(i):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    N_matrix = []
    for i in matrix:
        N_list = []
        for j in i:
            N_list.append(round(j/div, 2))
        N_matrix.append(N_list)
    return N_matrix
