'''Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

Letter	Number Range
"B"	    1-15
"I"	    16-30
"N"	    31-45
"G"	    46-60
"O"	    61-75'''


def get_bingo_letter(number):

    bingo_letters = ["B", "I", "N", "G", "O"]
    n = 1

    for index in range(len(bingo_letters)):
        if number in list(range(n, n + 15)):
            return bingo_letters[index]
        n += 15


print(get_bingo_letter(75))  # "O"
print(get_bingo_letter(54))  # "G"
print(get_bingo_letter(25))  # "I"
print(get_bingo_letter(38))  # "N"
print(get_bingo_letter(11))  # "B"
