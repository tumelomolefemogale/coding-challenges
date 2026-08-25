'''Given a number for the current floor of an elevator and an array of
requested floors, return an array of the order the elevator should visit
them to minimize number of floors travelled.

If tied, go up first.
Floors with a request must be visited when the elevator first passes them.'''


def elevator_stops(current_floor, requested_floors):
    negative_differences_floors = []
    positive_differences_floors = []
    for requested_floor in requested_floors:
        difference = current_floor - requested_floor
        if difference >= 0:
            positive_differences_floors.append((difference, requested_floor))
        else:
            negative_differences_floors.append((-difference, requested_floor))

    sorted_negatives = sorted(negative_differences_floors)
    sorted_positives = sorted(positive_differences_floors)

    if len(sorted_positives) == 0:
        return sorted([a for _, a in sorted_negatives])

    elif len(sorted_negatives) == 0:
        return sorted([a for _, a in sorted_positives], reverse=True)

    ordered_requests = []
    if sorted_positives[0][0] < sorted_negatives[0][0]:
        for _, a in sorted_positives:
            ordered_requests.append(a)

        for _, b in sorted_negatives:
            ordered_requests.append(b)

    elif (sorted_negatives[0][0] < sorted_positives[0][0]) or (sorted_negatives[0][0] == sorted_positives[0][0]):
        for _, c in sorted_negatives:
            ordered_requests.append(c)

        for _, d in sorted_positives:
            ordered_requests.append(d)

    return ordered_requests


print(elevator_stops(5, [2, 8, 3, 9]))
print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))
print(elevator_stops(1, [4, 8, 3, 6, 9]))
print(elevator_stops(12, [6, 10, 7, 3, 1, 4]))
print(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]))
