# Given a positive integer, determine whether it is a narcissistic number.
# A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
# For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.

def is_narcissistic(number):
    answer = 0
    num_str_list = list(str(number))
    for num_str in num_str_list:
        answer += int(num_str) ** len(num_str_list)

    return answer == number


print(is_narcissistic(153))
print(is_narcissistic(154))
print(is_narcissistic(371))
print(is_narcissistic(512))
print(is_narcissistic(9))
print(is_narcissistic(11))
print(is_narcissistic(9474))
print(is_narcissistic(6549))
