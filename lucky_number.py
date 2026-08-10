'''Given a string of a person's first and last name, calculate their lucky number using the following rules:

First and last names are separated by a space
Find the vowel and consonant count for each name
Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
Do the same for the two larger counts and the larger name
Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13.'''


def get_lucky_number(names):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    names_split = names.split()

    length1 = len(names_split[0])
    length2 = len(names_split[1])

    smaller_name = ''
    larger_name = ''

    if length1 > length2:
        smaller_name += names_split[1]
        larger_name += names_split[0]
    else:
        smaller_name += names_split[0]
        larger_name += names_split[1]

    vowel_counts = []
    consonant_counts = []

    for name in names_split:
        vowel_count = 0
        consonant_count = 0

        for letter in name:
            if letter not in vowels:
                consonant_count += 1
            else:
                vowel_count += 1

        vowel_counts.append(vowel_count)
        consonant_counts.append(consonant_count)

    vowel_counts_sorted = sorted(vowel_counts)
    consonant_counts_sorted = sorted(consonant_counts)

    product1 = vowel_counts_sorted[0] * consonant_counts_sorted[0] * len(smaller_name)
    product2 = vowel_counts_sorted[1] * consonant_counts_sorted[1] * len(larger_name)

    difference = abs(product1 - product2)

    if difference == 0:
        return 13
    else:
        return difference


print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis"))
print(get_lucky_number("James Wilson"))
print(get_lucky_number("Elizabeth Hernandez"))
print(get_lucky_number("Mike Walker"))
print(get_lucky_number("Chloe Perez"))
