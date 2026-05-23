# Given an array of objects, each with a "name" and "age" property,
# Return an array containing the name of the oldest person.
# If multiple people share the oldest age,
# Return all of their names in the order they appear in the input.


def get_oldest(array):
    if len(array) == 0:
        return 'This list is empty.'
    elif len(array) == 1:
        return [array[0]["name"]]
    else:
        sorted_array = sorted(array, key=lambda x: x["age"], reverse=True)

        oldest = []

        for person in sorted_array:
            if person['age'] == sorted_array[0]['age']:
                oldest.append(person['name'])

        return oldest


print(get_oldest([{"name": "Brenda", "age": 40}]))
print(get_oldest([{"name": "Alice", "age": 30},
                  {"name": "Bob", "age": 25}]))
print(get_oldest([{"name": "Allison", "age": 25},
                  {"name": "Bill", "age": 30},
                  {"name": "Carol", "age": 30}]))
print(get_oldest([{"name": "George", "age": 50},
                  {"name": "Shirley", "age": 42},
                  {"name": "Beth", "age": 48},
                  {"name": "Holly", "age": 50},
                  {"name": "Kevin", "age": 44},
                  {"name": "Frank", "age": 47},
                  {"name": "Zach", "age": 50},
                  {"name": "Jennifer", "age": 43}]))
