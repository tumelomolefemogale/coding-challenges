# Given an integer representing the number of candles you start with,
# and an integer representing burned candles it takes to create a new one,
# this program returns the number of candles used after creating and burning.

# For example, if given 7 candles, it takes 2 burned candles to make a new one:
# Burn 7 candles to get 7 leftovers,
# Recycle 6 leftovers into 3 new candles (1 leftover remains),
# Burn 3 candles to get 3 more leftovers (4 total),
# Recycle 4 leftovers into 2 new candles,
# Burn 2 candles to get 2 leftovers,
# Recycle 2 leftovers into 1 new candle,
# Burn 1 candle.
# You will have burned 13 total candles in the example.

def burn_candles(candles, leftovers_needed):
    candles_list = []
    remaining_candles_list = []

    while candles >= leftovers_needed:
        candles_list.append(candles)
        quotient = candles // leftovers_needed
        remainder = candles % leftovers_needed
        remaining_candles_list.append(remainder)

        candles = quotient + remainder

    candles_list.append(candles)

    if remaining_candles_list:
        candles_burnt = sum(candles_list) - sum(remaining_candles_list)
    elif remaining_candles_list == []:
        candles_burnt = sum(candles_list)

    return candles_burnt


print(burn_candles(7, 2))
print(burn_candles(10, 5))
print(burn_candles(20, 3))
print(burn_candles(17, 4))
print(burn_candles(2345, 3))
