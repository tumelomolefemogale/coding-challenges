'''Given an array of clue numbers and an array of cells, determine whether the cells satisfy the nonogram clue.
The clue is an array of numbers representing the lengths of consecutive filled cells, in order.
For example, a clue of [3, 2] means there should be 3 consecutive filled cells followed by 2 consecutive filled cells, separated by at least one empty cell.
The row is an array of 1s (filled) and 0s (empty).'''


def is_valid_nonogram(clues, cells):

    for num in [-1, 0]:
        while (cells[num] == 0):
            del cells[num]

    string = ''
    for cell in cells:
        string += str(cell)

    string_list = string.split('0')

    list1 = []
    for element in string_list:
        integers = 0
        for num in element:
            integers += int(num)
        list1.append(integers)

    list2 = []
    for num in list1:
        if num == 0:
            continue
        list2.append(num)

    return list2 == clues


print(is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]))
print(is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]))
print(is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]))
print(is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
