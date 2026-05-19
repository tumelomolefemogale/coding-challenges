# Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.
# If more than one element could be considered out of place, return the index of the first one.


def find_offender(array):

    if len(array) == 0:
        return None
    elif len(array) == 1:
        return 0
    elif len(array) == 2:
        if array[0] > array[1]:
            return 0
    elif len(array) >= 3:
        for index in range(len(array) - 2):
            if (array[index] < array[index + 1]) and (array[index + 1] > array[index + 2]):
                if array[index + 2] < array[index]:
                    return index + 2
                else:
                    return index + 1

        if array[-1] < array[-2]:
            return len(array) - 1


print(find_offender([1, 6, 2, 3, 4, 5]))
print(find_offender([1, 2, 3, 5, 4, 5]))
print(find_offender([2, 1]))
print(find_offender([2, 4, 1, 6, 8]))
print(find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]))
