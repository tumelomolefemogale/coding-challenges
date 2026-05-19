# Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

# For example, given:
# [["a", "b"],["a", "a"]]

# Return:
# [["b", "a"], ["b", "b"]]


def invert_matrix(matrix):

    new_array = []
    set_array = list(set(matrix[0]))

    for array in matrix:
        new_array.append(' ')
        for element in array:
            if element == set_array[0]:
                new_array.append(set_array[1])
            elif element == set_array[1]:
                new_array.append(set_array[0])

    del new_array[0]

    space_indices = []
    for index, element in enumerate(new_array):
        if element == ' ':
            space_indices.append(index)

    space_indices.append(len(new_array))

    new_matrix = []

    first_array = list(new_array[0:space_indices[0]])

    new_matrix.append(first_array)

    for num in range(len(matrix) - 1):
        other_array = list(new_array[space_indices[num] + 1:space_indices[num + 1]])
        new_matrix.append(other_array)

    return new_matrix


print(invert_matrix([["a", "b"], ["a", "a"]]))
print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]))
print(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]))
print(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]))
print(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]))
