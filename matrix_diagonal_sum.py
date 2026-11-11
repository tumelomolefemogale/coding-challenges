'''Given a square matrix, return the sum of both diagonals.
If the matrix has odd size, count the center element only once.'''

import math


def diagonal_sum(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    diagonal1_result = 0
    for i in range(len(matrix)):
        diagonal1_result += matrix[i][i]

    diagonal2_result = 0
    i = 1
    for j in range(len(matrix)):
        diagonal2_result += matrix[len(matrix) - i][j]
        i += 1

    if len(matrix) % 2 == 0:
        return diagonal1_result + diagonal2_result
    else:
        flattened = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                flattened.append(matrix[i][j])

        middle_num = flattened[math.floor(len(flattened) / 2)]

        return diagonal1_result + diagonal2_result - middle_num


print(diagonal_sum([[1, 2], [3, 4]]))

print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print(diagonal_sum([[5]]))
