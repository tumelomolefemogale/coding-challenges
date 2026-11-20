'''Given a string, return an array with the number of vowels and number of consonants in the string.
Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].'''

import string

punctuations_and_space_list = list(string.punctuation)

punctuations_and_space_list.append(' ')


def count(string):
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_count += 1
        elif char in punctuations_and_space_list:
            continue
        else:
            consonant_count += 1

    return [vowel_count, consonant_count]


print(count("Hello World"))
print(count("JavaScript"))
print(count("Python"))
print(count("freeCodeCamp"))
print(count("Hello, World!"))
print(count("The quick brown fox jumps over the lazy dog."))
