#!/usr/bin/python3
def pascal_triangle(n):
    triangle = [[1]]
    for rows in range(n - 1):
        triangle.append(
            [a + b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
