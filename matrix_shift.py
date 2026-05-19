# Given a matrix (array of arrays) of numbers and an integer, shift all values in the matrix by the given amount.
# A positive shift moves values to the right.
# A negative shift moves values to the left.

# For example, given:
# [[1, 2, 3], [4, 5, 6]]
# with a shift of 1, move all the numbers to the right one:
# [[6, 1, 2], [3, 4, 5]]


def shift_matrix(matrix, shift):
    new_array0 = []
    for array in matrix:
        for number in array:
            new_array0.append(number)

    new_array1 = []

    for num in range(len(new_array0)):
        new_array1.append(new_array0[(-shift + num) % len(new_array0)])

    new_matrix = [[] for _ in range(len(matrix))]

    for index in range(len(matrix)):
        for num in range(len(matrix[0])):
            new_matrix[index].append(new_array1[num])
        del new_array1[0:num + 1]

    return new_matrix


print(shift_matrix([[1, 2, 3], [4, 5, 6]], 1))
print(shift_matrix([[1, 2, 3], [4, 5, 6]], -1))
print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))
print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6))
print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7))
print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54))
