# Given an array of hours slept each night leading up to today, and a target number of hours per night
# Return how many hours of sleep you need tonight to eliminate your sleep debt.

# Include tonight's hours in the total time needed to catch up.
# If you've slept enough to cover tonight's target or more, return 0.


def sleep_debt(array, target):
    sleep_required = target * 7
    hours_slept = sum(array)

    debt = abs(sleep_required - hours_slept)

    return debt


print(sleep_debt([6, 6, 6, 6, 6, 6], 8))
print(sleep_debt([6, 7, 8, 4, 8, 6], 7))
print(sleep_debt([10, 10, 9, 10, 9, 11], 9))
print(sleep_debt([8, 7, 6, 7, 6, 8], 6))
print(sleep_debt([8, 9, 10, 9, 10, 7], 7))
