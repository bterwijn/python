list = [1023, 4009, 3005, 2011]
list.sort()
print(list)  # [1023, 2011, 3005, 4009]


def last_two_digits(value):
    return value % 100

list.sort(key=last_two_digits)
print(list)  # [3005, 4009, 2011, 1023]


def distance_to_2000(value):
    return abs(2000 - value)

list.sort(key=distance_to_2000)
print(list)  # [2011, 1023, 3005, 4009]
