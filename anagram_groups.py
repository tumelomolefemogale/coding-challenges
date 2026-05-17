# Given an array of words, return a 2d array of the words grouped into anagrams.
# Words are anagrams if they contain the same letters in any order.
# Each word belongs to exactly one group.
# Return order doesn't matter.
# For example, given ["listen", "silent", "hello", "enlist", "world"],
# returns [["listen", "silent", "enlist"], ["hello"], ["world"]].

def group_anagrams(array):

    sorted_array = []
    for word in array:
        sorted_array.append(''.join(sorted(word)))

    array0 = []
    array1 = []
    for index1 in range(len(array)):
        for index2 in range(len(array)):
            if sorted_array[index1] == sorted_array[index2]:
                array0.append(array[index1])
                array1.append(sorted_array[index1])

    array2 = []
    for index, word in enumerate(array1):
        array2.append((index, word))

    setted_list = list(set(array1))

    arrays = [[] for _ in range(len(list(set(array1))))]
    for num in range(len(setted_list)):
        for index, word in array2:
            if word == setted_list[num]:
                arrays[num].append(array0[index])

    arrays = [list(set(array)) for array in arrays]

    return arrays


print(group_anagrams(["listen", "silent", "hello", "enlist", "world"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]))
print(group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]))
