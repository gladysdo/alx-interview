#!/usr/bin/python3
"""
Take a number of rows to be printed, lets assume it to be n
Make outer iteration i from 0 to n times to print the rows.
Make inner iteration for j from 0 to (N – 1).
Print single blank space ” “.
Close inner loop (j loop) //its needed for left spacing.
Make inner iteration for j from 0 to i.
Print nCr of i and j.
Close inner loop.
Print newline character () after each inner iteration
"""

def pascal_triangle(n):
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
