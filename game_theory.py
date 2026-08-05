'''Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].
The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
Each character represents one round, scored as follows:
If both players cooperate, each scores 3.
If both players defect, each scores 1.
If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.'''


def play_game(a, b):
    array = []
    player1_score = 0
    player2_score = 0

    for index in range(len(a)):
        if a[index] == 'C' and b[index] == 'C':
            player1_score += 3
            player2_score += 3
        elif a[index] == 'D' and b[index] == 'D':
            player1_score += 1
            player2_score += 1
        elif a[index] == 'C' and b[index] == 'D':
            player2_score += 5
        else:
            player1_score += 5

    array.append(player1_score)
    array.append(player2_score)

    return array


print(play_game("CCCC", "CCCC"))
print(play_game("DDDD", "DDDD"))
print(play_game("CCDD", "CDDD"))
print(play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD"))
print(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"))
