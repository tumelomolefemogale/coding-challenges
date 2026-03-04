# Given a secret message, this program returns the decoded string.
# The given integer represents the number of times each letter was shifted.

import string


def decode(message, shift):

    letters_lowercase = string.ascii_lowercase

    new_word_lowercase = ''

    for char in message:
        if char.isalpha():
            if char == char.upper():
                char = char.lower()
            letter_index = letters_lowercase.index(char)
            new_letter_index = letter_index - shift
            if IndexError:
                new_letter_index = new_letter_index % len(letters_lowercase)
            char = letters_lowercase[new_letter_index]
            new_word_lowercase += char
        else:
            new_word_lowercase += char

    new_word_properly_cased = ''

    for a, b in zip(message, new_word_lowercase):
        if a == a.upper():
            new_word_properly_cased += b.upper()
        else:
            new_word_properly_cased += b

    return new_word_properly_cased


print(decode("Xlmw mw e wigvix qiwweki.", 4))
print(decode("Byffi Qilfx!", 20))
print(decode("Zqd xnt njzx?", -1))
print(decode("Tfuvtruvdp", -9))
