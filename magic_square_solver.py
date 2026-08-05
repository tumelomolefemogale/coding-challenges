'''Given a 3x3 grid with one missing number (represented as 0)
Return the missing number that completes the magic square, or "impossible" if no valid number exists.
A magic square is a grid where every row, column, and diagonal adds up to the same number.'''


def solve_magic_square(grid):
    sums = []
    for array in grid:
        sums.append(sum(array))

    if sums[0] == sums[1]:
        return abs(sums[1] - sums[2])
    elif sums[0] == sums[2]:
        return abs(sums[2] - sums[1])
    elif sums[1] == sums[2]:
        return abs(sums[2] - sums[0])
    else:
        return "impossible"


print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))  # 5
print(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]))  # 4
print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))  # 16
print(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]))  # 39
print(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]))  # "impossible"
