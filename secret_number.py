# Given a secret number and a guess, determine if the guess is correct.
# Return:
#   "higher" if the secret number is higher than the guess.
#   "lower" if the secret number is lower than the guess.
#   "you got it!" if the guess is correct.

def guess_number(secret, guess):
    if secret > guess:
        return 'higher'
    elif secret < guess:
        return 'lower'
    else:
        return 'you got it!'

print(guess_number(50, 30))
print(guess_number(85, 99))
print(guess_number(2026, 2026))
print(guess_number(92904, 11283))
print(guess_number(230495, 423920))
print(guess_number(120349, 120349))