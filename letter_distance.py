'''Given two strings of equal length, return the sum of the shortest distances between each pair of characters.
The input will only contain lowercase letters
The alphabet is treated as a circle, so the distance between a and z is 1.'''


import string

lowercase_letters = string.ascii_lowercase

negative_indices = [num for num in range(-26, 0, 1)]


def letter_distance(string1, string2):
    forward_distances = []
    backward_distances = []

    for element1, element2 in zip(string1, string2):
        element1_index = lowercase_letters.find(element1)
        element2_index1 = lowercase_letters.find(element2)

        forward_distance = abs(element2_index1 - element1_index)
        forward_distances.append(forward_distance)

        element2_index2 = negative_indices[element2_index1]
        backward_distance = abs(element2_index2 - element1_index)
        backward_distances.append(backward_distance)

    forward_distances_sum = sum(forward_distances)
    backward_distances_sum = sum(backward_distances)

    if forward_distances_sum < backward_distances_sum:
        return forward_distances_sum
    else:
        return backward_distances_sum


print(letter_distance("abc", "bcd"))
print(letter_distance("abc", "xyz"))
print(letter_distance("encrypt", "decrypt"))
print(letter_distance("algorithm", "codeblock"))
print(letter_distance("lobster", "penguin"))
print(letter_distance("alligator", "crocodile"))
