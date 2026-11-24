'''Given two integers, return the least common multiple (LCM) of the two numbers.
The LCM of two numbers is the smallest positive integer that is a multiple of both numbers.

For example, given 4 and 6, return 12 because:
Multiples of 4 are 4, 8, 12 and so on.
Multiples of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.'''


def lcm(int1, int2):

    min_value = min(int1, int2)
    max_value = max(int1, int2)

    min_value_multiples = [min_value]
    max_value_multiples = [max_value]

    for i in range(min_value * max_value):
        max_value_multiples.append(max_value_multiples[i] + max_value)
        min_value_multiples.append(min_value_multiples[i] + min_value)

        if min_value_multiples[i] in max_value_multiples:
            return min_value_multiples[i]


print(lcm(4, 6))
print(lcm(9, 6))
print(lcm(10, 100))
print(lcm(13, 17))
print(lcm(45, 70))
