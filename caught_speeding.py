'''Given an array of numbers representing the speed at which vehicles were observed traveling,
and a number representing the speed limit, return an array with two items,
the number of vehicles that were speeding,
followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].'''


def speeding(array, limit):
    speeding_vehicles = 0
    amounts_beyond_limit = 0

    for num in array:
        if num > limit:
            speeding_vehicles += 1
            amounts_beyond_limit += (num - limit)

    if speeding_vehicles == 0:
        return [0, 0]
    else:
        amounts_beyond_limit_avg = amounts_beyond_limit / speeding_vehicles
        return [speeding_vehicles, amounts_beyond_limit_avg]


print(speeding([50, 60, 55], 60))
print(speeding([58, 50, 60, 55], 55))
print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([100, 105, 95, 102], 100))
print(speeding([40, 45, 44, 50, 112, 39], 55))
