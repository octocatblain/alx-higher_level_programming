#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix of similar sized rows"""

    message = "matrix must be a matrix (list of lists) of integers/floats"
    new = []
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(message)
    if type(div) is not int and type(div) is not float and div is not None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(message)
    for i in range(len(matrix)):
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new.append([])
        for j in matrix[i]:
            if type(j) is int or type(j) is float:
                new[i].append(round(j / div, 2))
            else:
                raise TypeError(message)
    return new
