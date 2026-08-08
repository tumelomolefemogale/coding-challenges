'''Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).

Numbers divisible by 3 count as a fizz.
Numbers divisible by 5 count as a buzz.
Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
Return an object or dictionary with the counts in the format: { fizz, buzz }.'''


def fizz_buzz_count(start, end):
    fizz = 0
    buzz = 0
    fizz_buzz = {}

    for num in range(start, end + 1):
        if (num % 3 == 0) and (num % 5 == 0):
            fizz += 1
            buzz += 1
        elif num % 3 == 0:
            fizz += 1
        elif num % 5 == 0:
            buzz += 1

    fizz_buzz['fizz'] = fizz
    fizz_buzz['buzz'] = buzz

    return fizz_buzz


print(fizz_buzz_count(1, 11))
print(fizz_buzz_count(14, 41))
print(fizz_buzz_count(24, 100))
print(fizz_buzz_count(-635, -14))
print(fizz_buzz_count(-5432, 6789))
