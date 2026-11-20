'''Given a string of digits, return 'true' if it is valid under the ISBN-10 check, otherwise 'false'.
An ISBN-10 has 10 characters.
Multiply the first digit by 10, the second by 9, and so on down to the last by 1,
then add everything up.
The number is valid if the total is divisible by 11.'''


def is_valid_isbn(string):

    from_ten_to_one = list(range(10, 0, -1))
    potential_isbn_list = [int(i) for i in string]

    products = []

    for num1, num2 in zip(from_ten_to_one, potential_isbn_list):
        products.append(num1 * num2)

    products_sum = sum(products)

    return products_sum % 11 == 0


print(is_valid_isbn("0306406152"))
print(is_valid_isbn("0471958697"))
print(is_valid_isbn("0306406153"))
print(is_valid_isbn("1234567890"))
print(is_valid_isbn("030640615"))
