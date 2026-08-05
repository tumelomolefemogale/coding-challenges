'''Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team,
Determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.'''


import string

alphabet_letters = string.ascii_letters


def battle(sentence1, sentence2):
    sentence1 = sentence1.replace(' ', '')
    sentence2 = sentence2.replace(' ', '')

    full_value1 = 0
    full_value2 = 0

    for letter1, letter2 in zip(sentence1, sentence2):
        letter_value1 = alphabet_letters.find(letter1) + 1
        full_value1 += letter_value1

        letter_value2 = alphabet_letters.find(letter2) + 1
        full_value2 += letter_value2

    if full_value1 > full_value2:
        return "We win"
    elif full_value1 == full_value2:
        return "Draw"
    else:
        return "We lose"


print(battle("hello world", "hello word"))
print(battle("Hello world", "hello world"))
print(battle("lorem ipsum", "kitty ipsum"))
print(battle("hello world", "world hello"))
print(battle("git checkout", "git switch"))
print(battle("Cheeseburger with fries", "Cheeseburger with Fries"))
print(battle("We must never surrender", "Our team must win"))
