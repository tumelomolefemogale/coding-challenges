'''Given a string of commands, return the final position and facing
direction of a robot as a tuple (x, y, direction).

The robot starts at (0, 0) facing "N". Moving north increases y,
moving east increases x.

"F" moves forward one step, "L" turns 90 degrees left, "R" turns
90 degrees right. Ignore any other characters.'''


def robot_walk(commands):

    directions = "NESW"
    directions_track = ["N"]

    x = 0
    y = 0

    for command in commands:
        if command == "R":
            directions_track.append(directions[(directions.index(directions_track[-1]) + 1) % len(directions)])
        elif command == "L":
            directions_track.append(directions[(directions.index(directions_track[-1]) - 1) % len(directions)])
        elif command == "F":
            if directions_track[-1] == "N":
                y += 1
            elif directions_track[-1] == "S":
                y -= 1
            elif directions_track[-1] == "E":
                x += 1
            elif directions_track[-1] == "W":
                x -= 1

    return x, y, directions_track[-1]


print(robot_walk("FFRFF"))
print(robot_walk("LLF"))
print(robot_walk(""))
print(robot_walk("FRFRFRF"))
print(robot_walk("LFLFLFLF"))
print(robot_walk("FxRyF!"))
