# Given two strings, return a new string that interleaves their characters one at a time.
# If one string is longer, append the remaining characters at the end.

# Begin with the first character of the first string.


def zip_strings(string1, string2):

    if len(string1) == len(string2):
        new_string = ''

        for num in range(len(string1)):
            new_string += string1[num]
            new_string += string2[num]

        return new_string
    else:
        if len(string1) > len(string2):
            small_string = string2
        else:
            small_string = string1

        string1_list = list(string1)
        string2_list = list(string2)

        new_string = ''

        for num in range(len(small_string)):
            new_string += string1[num]
            new_string += string2[num]
            del string1_list[0]
            del string2_list[0]

        if (len(string1_list) == 0) and (len(string2_list) > 0):
            main_string_list = string2_list
        elif (len(string1_list) > 0) and (len(string2_list) == 0):
            main_string_list = string1_list

        for element in main_string_list:
            new_string += element

        return new_string


print(zip_strings("abc", "123"))
print(zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz"))
print(zip_strings("day", "night"))
print(zip_strings("python", "javascript"))
print(zip_strings("feCdCm", "reoeap"))
