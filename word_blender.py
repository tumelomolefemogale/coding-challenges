'''Given two words, return a new word by combining the first half of the first word with the second half of the second word.
For odd-length words, the first half is the shorter half.'''

import math


def blend_words(a, b):
    first_half = a[0:math.floor(len(a) / 2)]
    second_half = b[math.floor(len(b) / 2):]
    return first_half + second_half


print(blend_words("turtle", "toucan"))  # "turcan"
print(blend_words("chipmunk", "flamingo"))  # "chipingo"
print(blend_words("falcon", "pelican"))  # "falican"
print(blend_words("hyena", "iguana"))  # "hyana"
print(blend_words("scorpion", "gorilla"))  # "scorilla"
print(blend_words("platypus", "wolverine"))  # "platerine"
