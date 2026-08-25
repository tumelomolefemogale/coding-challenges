'''Given a 2D matrix, return a flat array with all of its values in clockwise order.
The returned array should have the top-left value first, move right along the top row,
then down the right column, then left along the bottom row,
then up the left column. Repeat inward for any remaining layers.
For example, given:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Return [1, 2, 3, 6, 9, 8, 7, 4, 5].'''


def spiral_matrix(matrix):
    flat_array = []

    while len(matrix) >= 2:
        for i in range(len(matrix[0])):
            flat_array.append(matrix[0][i])
        del matrix[0]

        for i in range(len(matrix)):
            flat_array.append(matrix[i][-1])
            del matrix[i][-1]

        for i in range(-1, -len(matrix[-1]) - 1, -1):
            flat_array.append(matrix[-1][i])
        del matrix[-1]

        for i in range(-1, -len(matrix) - 1, -1):
            flat_array.append(matrix[i][0])
            del matrix[i][0]

    if matrix:
        flat_array.extend(matrix[0])

    return flat_array


print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]]))
print(spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]]))
print(spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]]))
