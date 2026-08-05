'''Given a 3x3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.
Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.'''


def tic_tac_toe(grid):
    for index in range(len(grid)):
        if (grid[index % len(grid)][index % len(grid)] == grid[(index + 1) % len(grid)][index % len(grid)]) and (grid[(index + 1) % len(grid)][index % len(grid)] == grid[(index + 2) % len(grid)][index % len(grid)]):
            return f"{grid[index % len(grid)][index % len(grid)]} wins"

    for index in range(len(grid)):
        if (grid[index % len(grid)][index % len(grid)] == grid[index % len(grid)][(index + 1) % len(grid)]) and (grid[index % len(grid)][(index + 1) % len(grid)] == grid[index % len(grid)][(index + 2) % len(grid)]):
            return f"{grid[index % len(grid)][index % len(grid)]} wins"
        if (grid[index % len(grid)][index % len(grid)] == grid[(index + 1) % len(grid)][(index + 1) % len(grid)]) and (grid[(index + 1) % len(grid)][(index + 1) % len(grid)] == grid[(index + 2) % len(grid)][(index + 2) % len(grid)]):
            return f"{grid[index % len(grid)][index % len(grid)]} wins"
        if (grid[(index + 2) % len(grid)][index % len(grid)] == grid[(index + 1) % len(grid)][(index + 1) % len(grid)]) and (grid[(index + 1) % len(grid)][(index + 1) % len(grid)] == grid[index % len(grid)][(index + 2) % len(grid)]):
            return f"{grid[(index + 2) % len(grid)][index % len(grid)]} wins"
        else:
            return "Draw"


print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))  # "X wins"
print(tic_tac_toe([["O", "O", "X"], ["X", "O", "X"], ["O", "X", "X"]]))  # "X wins"
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))  # "Draw"
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "O"], ["O", "O", "X"]]))  # "O wins"
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))  # "X wins"
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))  # "Draw"
