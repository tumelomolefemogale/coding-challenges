# Given two integers, round the first to the nearest multiple of the second.

def round_to_nearest_multiple(a, b):

    quotient = a / b

    quotient_str_list = [c for c in str(quotient).split('.')]

    if int(quotient_str_list[1][0]) >= 5:
        multiplier = int(quotient_str_list[0]) + 1
    else:
        multiplier = int(quotient_str_list[0])

    return b * multiplier


print(round_to_nearest_multiple(5, 3))
print(round_to_nearest_multiple(17, 4))
print(round_to_nearest_multiple(43, 5))
print(round_to_nearest_multiple(38, 11))
print(round_to_nearest_multiple(93, 12))
