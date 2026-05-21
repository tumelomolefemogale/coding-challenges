# Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it.
# For instance, given [[1, 2], [3, 4]], which looks like this:
# [
#  [1, 2],
#  [3, 4]
# ]
# You should return [[3, 1], [4, 2]], which looks like this:
# [
#  [3, 1]
#  [4, 2]
# ]


def rotate(matrix):
    new_matrix = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix) - 1, -1, -1):
            new_matrix[i].append(matrix[j][i])

    return new_matrix


print(rotate([[1]]))
print(rotate([[1, 2], [3, 4]]))
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]))
