# Acquire correct input from user
creditCard_num = input('Dear User, what is your credit card number? ').strip()
while not (creditCard_num.isdigit() and 13 <= len(creditCard_num) <= 19):
    creditCard_num = input('''
\tYOU HAVE ENTERED INVALID INPUT!
Please enter your credit card number here. ''').strip()

# Store each digit as an element in 'num_list'
num_str_list = list(creditCard_num)
nested_list = []

index0 = -1
count0 = 0

# Reverse the order of elements in 'num_list'
# Enumerate each element and store it in 'nested_list'
for _ in num_str_list:
    nested_list.append([count0, num_str_list[index0]])
    index0 -= 1
    count0 += 1

new_list = []

# Use a loop and conditionals to do the required math
# Store the results in 'new_list'
for index1, num_str in nested_list:
    if index1 % 2 != 0:
        product = int(num_str) * 2
        if product > 9:
            difference = product - 9
            nested_list[index1][1] = difference
            new_list.append(difference)
        else:
            nested_list[index1][1] = product
            new_list.append(product)

    else:
        new_list.append(int(num_str))

# Print out the appropriate message
if sum(new_list) % 10 == 0:
    print(f'\n{creditCard_num} is a valid credit card number.')
else:
    print(f'\n{creditCard_num} is NOT a valid credit card number.')
