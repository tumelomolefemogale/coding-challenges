'''Given a sentence string, return an array with a count of each character in alphabetical order.
Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string.'''


import string

alphabets = string.ascii_lowercase


def count_characters(string):
    count_list = []
    sorted_lowercase_string = sorted(string.lower())
    for letter in sorted_lowercase_string:
        if letter not in alphabets:
            continue
        count_list.append(f"{letter} {sorted_lowercase_string.count(letter)}")

    return list(sorted(set(count_list)))


print(count_characters("hello world"))
print(count_characters("I love coding challenges!"))
print(count_characters("// TODO: Complete this challenge ASAP!"))
