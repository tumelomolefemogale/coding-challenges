'''Given a number, determine whether it is a pronic number.
A pronic number is the product of two consecutive integers.
For example, 6 is pronic because 2 * 3 = 6.'''


def is_pronic(product):
    if product == 0:
        return True

    integers = []

    for number in range(product):
        if number * (number + 1) == product:
            integers.append(number)
            integers.append(number + 1)
        else:
            None

    if not integers:
        return False
    elif len(integers) > 0:
        return True


print(is_pronic(6))
print(is_pronic(15))
print(is_pronic(12))
print(is_pronic(132))
print(is_pronic(80))
print(is_pronic(0))
