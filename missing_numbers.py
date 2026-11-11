'''Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).
The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.'''


def find_missing_numbers(array):

    sorted_array = sorted(array)
    missing_numbers = []
    for num in range(1, sorted_array[-1] + 1):
        if num not in array:
            missing_numbers.append(num)

    return sorted(missing_numbers)


print(find_missing_numbers([1, 3, 5]))
print(find_missing_numbers([1, 2, 3, 4, 5]))
print(find_missing_numbers([1, 10]))
print(find_missing_numbers([10, 1, 10, 1, 10, 1]))
print(find_missing_numbers([3, 1, 4, 1, 5, 9]))
print(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]))
