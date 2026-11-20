'''Given two positive integers, return their greatest common divisor (GCD).
The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
For example, the divisors of 4 are 1, 2, and 4.
The divisors of 6 are 1, 2, 3, and 6.
So given 4 and 6, return 2, the largest number that appears in both sets of divisors.'''


def gcd(int1, int2):
    array1 = []

    for h in [int1, int2]:
        for i in range(1, h + 1):
            if h % i == 0:
                array1.append(i)

    array2 = []
    sorted_array1 = sorted(array1)
    for j in range(len(sorted_array1)):
        if j == len(sorted_array1) - 1:
            break
        if sorted_array1[j] == sorted_array1[j + 1]:
            array2.append(sorted_array1[j])

    return array2[-1]


print(gcd(4, 6))
print(gcd(20, 15))
print(gcd(13, 17))
print(gcd(654, 456))
print(gcd(3456, 4320))
