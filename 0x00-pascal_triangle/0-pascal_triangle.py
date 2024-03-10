#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the n number of rows.

    Args:
    - n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    - list of lists: A list of lists representing Pascal's Triangle.
                     Each inner list corresponds to a row in the triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle