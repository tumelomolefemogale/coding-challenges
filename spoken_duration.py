'''Given a number of seconds, return the duration in spoken English.
Break the duration into hours, minutes, and seconds.
Skip any zero values.
Use singular or plural as appropriate ("1 hour", "2 hours").
If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds").'''

import math


def get_spoken_duration(seconds):
    if seconds >= 3600:
        hours = seconds / 3600
        if hours == math.floor(hours):
            return f"{math.floor(hours)} hour(s)"

        remaining_minutes = (hours - math.floor(hours)) * 60
        if remaining_minutes == math.floor(remaining_minutes):
            return f"{math.floor(hours)} hour(s) and {math.floor(remaining_minutes)} minutes"

        remaining_seconds = (remaining_minutes - math.floor(remaining_minutes)) * 60
        if remaining_seconds > 0:
            return f"{math.floor(hours)} hour(s), {math.floor(remaining_minutes)} minute(s) and {round(remaining_seconds)} second(s)"

    elif 59 < seconds < 3600:
        minutes = seconds / 60
        if minutes == math.floor(minutes):
            return f"{minutes} minute(s)"

        remaining_seconds = (minutes - math.floor(minutes)) * 60
        if remaining_seconds > 0:
            return f"{math.floor(minutes)} minute(s) and {round(remaining_seconds)} second(s)"

    else:
        return f"{seconds} second(s)"


print(get_spoken_duration(3723))
print(get_spoken_duration(7295))
print(get_spoken_duration(8521))
print(get_spoken_duration(435))
print(get_spoken_duration(14455))
print(get_spoken_duration(72000))
print(get_spoken_duration(1))
