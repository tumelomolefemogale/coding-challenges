# Given an array of numbers, return a new array containing the value needed to get from each number to the next number.
# For the last number, use 0 since there is no next number.
# For example, given [1, 2, 4, 7], return [1, 2, 3, 0].


def find_differences(array):
    differences = []
    for index in range(len(array) - 1):
        difference = array[index + 1] - array[index]
        differences.append(difference)

    differences.append(0)

    return differences


print(find_differences([1, 2, 4, 7]))
print(find_differences([10, 15, 19, 22, 24, 25]))
print(find_differences([25, 20, 16, 13, 11, 10]))
print(find_differences([0, 1, 2, 2, 3, 3, 4, 5]))
print(find_differences([1, 2, 5, 12, 34, -15, -1, 41, 113, -222, -99, -40, 10, -18, -6, -2, -1]))
