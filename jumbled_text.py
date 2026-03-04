# This program returns a jumbled version of a string.

# The first and last letters of the words remain in place
# All letters between the first and last letter are sorted alphabetically.
# NOTE: the text MUST be lowercase with no punctuations

def jbelmu(text):
    text_list = text.split(" ")
    list0 = []
    list1 = []

    for word in text_list:
        list0.append(list(word))

    for word_list in list0:
        if len(word_list) > 3:
            first_letter = word_list.pop(0)
            last_letter = word_list.pop()

            sorted_middle_letters = "".join(sorted(word_list))
            new_word = first_letter + sorted_middle_letters + last_letter

            list1.append(new_word)
        else:
            unjumbled_word = "".join(word_list)
            list1.append(unjumbled_word)

    new_text = " ".join(list1)

    return new_text


print(jbelmu("hello world"))
print(jbelmu("i love jumbled text"))
print(jbelmu("freecodecamp is my favorite place to learn to code"))
print(jbelmu("the quick brown fox jumps over the lazy dog"))
