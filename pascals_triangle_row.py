'''Given an integer n, return the nth row of Pascal's triangle as an array.
In Pascal's Triangle, each row begins and ends with 1,
and each interior value is the sum of the two values directly above it.
Here are the first 5 rows of the triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1'''


def pascal_row(n):
    full_array = [[1], [1, 1]]

    if n <= 0:
        return None
    elif n == 1:
        return full_array[0]
    elif n == 2:
        return full_array[1]
    else:
        for i in range(1, n - 1):
            small_array = []
            small_array.append(1)
            while len(full_array[i]) >= 2:
                answer = full_array[i][0] + full_array[i][1]
                small_array.append(answer)
                del full_array[i][0]
            small_array.append(1)
            full_array.append(small_array)
        return full_array[-1]


print(pascal_row(5))
print(pascal_row(3))
print(pascal_row(1))
print(pascal_row(10))
print(pascal_row(15))
