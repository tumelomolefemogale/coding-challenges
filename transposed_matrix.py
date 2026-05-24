# Given a matrix (an array of arrays), return the transposed version of it.
# To transpose the matrix, swap the rows and columns.
# E.g: a value at index [0, 1] should move to index [1, 0].

# For example, given:
# [
#  [1, 2, 3],
#  [4, 5, 6]
# ]

# Return:
# [
#  [1, 4],
#  [2, 5],
#  [3, 6]
# ]


def transpose(matrix):
    new_matrix = [[] for _ in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])

    return new_matrix


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1, 2], [3, 4], [5, 6]]))
print(transpose([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]))
print(transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]]))
