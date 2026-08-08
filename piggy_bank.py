'''Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".

The object may contain any of the following:

Coin	  Value
pennies	  $0.01
nickels	  $0.05
dimes	  $0.10
quarters  $0.25
'''


def piggy_bank(object):
    amount = 0
    for item in object:
        if item == "pennies":
            amount += (0.01 * object[item])
        if item == "nickels":
            amount += (0.05 * object[item])
        if item == "dimes":
            amount += (0.10 * object[item])
        if item == "quarters":
            amount += (0.25 * object[item])

    return f"${round(amount, 2)}"


print(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}))
print(piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}))
print(piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}))
print(piggy_bank({}))
print(piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}))
