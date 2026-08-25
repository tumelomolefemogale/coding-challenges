# Given an array of numbers where all but one number follow a pattern,
# Return a new array with the one number that doesn't follow the pattern fixed.

# The pattern will be one of:
# The numbers increase from one to the next by a fixed amount (addition).
# The numbers decrease from one to the next by a fixed amount (subtraction).
# For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].


def fix_prank_number(array):
    amount = 0
    differences = []

    for a in range(len(array) - 1):
        difference = array[a + 1] - array[a]
        if difference in differences:
            amount += difference
            break
        differences.append(difference)

    if amount == differences[0]:
        new_array = [array[0]]
        for b in range(len(array) - 1):
            new_array.append(new_array[b] + amount)
    elif amount == differences[-1]:
        new_array = [array[-1]]
        for _ in range(-1, -len(array), -1):
            new_array.append(new_array[-1] - amount)
        if new_array == sorted(new_array):
            new_array = sorted(new_array, reverse=True)
        else:
            new_array = sorted(new_array)

    return new_array


print(fix_prank_number([2, 4, 7, 8, 10]))
print(fix_prank_number([10, 10, 8, 7, 6]))
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
print(fix_prank_number([4, 1, -2, -5, -8, -5]))
print(fix_prank_number([0, 100, 200, 300, 150, 500]))
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
print(fix_prank_number([-5, 5, 10, 15, 20]))
