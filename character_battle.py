# Given two strings representing your army and an opposing army,
# each character from your army battles the character,
# at the same position from the opposing army

# Characters a-z have a strength of 1-26, respectively.
# Characters A-Z have a strength of 27-52, respectively.
# Digits 0-9 have a strength of their face value.
# All other characters have a value of zero.

# Each character can only fight one battle.
# For each battle, the stronger character wins.
# The army with more victories, wins the war.

import string

all_letters = string.ascii_letters


def battle(my_army, opposing_army):

    for my_char, opposing_char in zip(my_army, opposing_army):
        if my_char.isalpha():
            my_char_strength = all_letters.index(my_char) + 1
            opposing_char_strength = all_letters.index(opposing_char) + 1
        elif my_char.isdigit():
            my_char_strength = my_char
            opposing_char_strength = opposing_char
        elif my_char in ['@', '$', '!', '.', ' ']:
            continue

        if my_char_strength > opposing_char_strength:
            my_army_battles_won.append(1)
        elif opposing_char_strength > my_char_strength:
            opposing_army_battles_won.append(1)

    if len(my_army) > len(opposing_army):
        return 'Opponent retreated'

    elif len(opposing_army) > len(my_army):
        return 'We retreated'

    elif len(opposing_army) == len(my_army):
        if sum(my_army_battles_won) > sum(opposing_army_battles_won):
            return 'We won'
        elif sum(opposing_army_battles_won) > sum(my_army_battles_won):
            return 'We lost'
        elif sum(opposing_army_battles_won) == sum(my_army_battles_won):
            return 'It was a tie'


my_army_battles_won = []
opposing_army_battles_won = []


print(battle("Hello", "World"))
print(battle("pizza", "salad"))
print(battle("C@T5", "D0G$"))
print(battle("kn!ght", "orc"))
print(battle("PC", "Mac"))
print(battle("Wizards", "Dragons"))
print(battle("Mr. Smith", "Dr. Jones"))
