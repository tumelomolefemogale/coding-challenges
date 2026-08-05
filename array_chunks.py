'''Given an array and a chunk size, return the array split into sub-arrays of that size.
The last chunk may be smaller if the array does not divide evenly.'''


def chunk_array(array, size):
    chunks = []

    while len(array) > size:
        chunks.append(array[:size])
        del array[:size]

    if len(array) <= size:
        chunks.append(array)

    return chunks


print(chunk_array([1, 2, 3, 4, 5, 6], 3))
print(chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2))
print(chunk_array([1, 2, 3, 4, 5], 3))
print(chunk_array(["a", "b", "c", "d", "e"], 1))
print(chunk_array([1, 2, 3], 5))
