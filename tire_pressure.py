'''Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle,
and another array of two numbers representing the minimum and maximum pressure for your tires in bar,
return an array of four strings describing each tire's status.

1 bar equals 14.5038 psi.
Return an array with the following values for each tire:

"Low" if the tire pressure is below the minimum allowed.
"Good" if it's between the minimum and maximum allowed.
"High" if it's above the maximum allowed.'''


def tire_status(array1, array2):
    min_pressure = array2[0] * 14.5038
    max_pressure = array2[1] * 14.5038

    strings_list = []

    for pressure in array1:
        if pressure < min_pressure:
            strings_list.append("Low")
        elif min_pressure < pressure < max_pressure:
            strings_list.append("Good")
        else:
            strings_list.append("High")

    return strings_list


print(tire_status([32, 28, 35, 29], [2, 3]))
print(tire_status([32, 28, 35, 30], [2, 2.3]))
print(tire_status([29, 26, 31, 28], [2.1, 2.5]))
print(tire_status([31, 31, 30, 29], [1.5, 2]))
print(tire_status([30, 28, 30, 29], [1.9, 2.1]))
