'''Given a string of numbers separated by commas,
return an array of the numbers sorted from smallest to largest.'''


def sort_numbers(string):
    numbers = [int(number) for number in string.split(',')]

    while numbers != sorted(numbers):
        for index in range(-len(numbers), -1, 1):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

    return numbers


print(sort_numbers("3,1,2"))
print(sort_numbers("5,3,8,1,9,2"))
print(sort_numbers("12,61,49,80,19,50,77,38"))
print(sort_numbers("0,6,-19,44,-2,7,0"))
