'''Given a matrix (an array of arrays) of single letters and a word to find.
Return the start and end indices of the word in the matrix.
The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.

The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top

For example, given the matrix:
[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:
[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word),
and [2, 1] are the indices for the "t" (end of the word).'''


def find_word(matrix, target):
    joined = []
    for row in matrix:
        string = ''.join(row)
        joined.append(string)

    for string in joined:
        reversed_string = ''.join(list(reversed(string)))
        if target in string or target in reversed_string:
            for row in range(len(matrix)):
                string1 = ''
                for col in range(len(matrix[row])):
                    string1 += matrix[row][col]

                first_letter_index = string1.find(target[0])
                last_letter_index = string1.find(target[-1])

                reversed_string = ''.join(list(reversed(string1)))
                if string1[:len(target)] == target:
                    return [[row, first_letter_index], [row, last_letter_index]]

                elif reversed_string[0:len(target)] == target:
                    return [[row, first_letter_index], [row, last_letter_index]]

        else:
            array1 = []
            for row in range(len(matrix)):
                string2 = ''
                for col in range(len(matrix[row])):
                    string2 += matrix[col][row]
                array1.append(string2)

            for col in range(len(array1)):
                reversed_col = ''.join(list(reversed(array1[col])))
                if array1[col][:len(target)] == target or reversed_col[:len(target)] == target:
                    first_letter_index = array1[col].find(target[0])
                    last_letter_index = array1[col].find(target[-1])
                    return [[first_letter_index, col], [last_letter_index, col]]


print(find_word([["a", "c", "t"],
                 ["t", "a", "t"],
                 ["c", "t", "c"]], "cat"))

print(find_word([["d", "o", "g"],
                 ["o", "g", "d"],
                 ["d", "g", "o"]], "dog"))

print(find_word([["h", "i", "s", "h"],
                 ["i", "s", "f", "s"],
                 ["f", "s", "i", "i"],
                 ["s", "h", "i", "f"]], "fish"))

print(find_word([["f", "x", "o", "x"],
                 ["o", "x", "o", "f"],
                 ["f", "o", "f", "x"],
                 ["f", "x", "x", "o"]], "fox"))
