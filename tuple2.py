import math

person = ("James", "Taylor", 73, 65.5)  # heterogeneous
print(len(person))  # 4
print(person)       # ('James', 'Taylor', 73, 65.5)

line = ((0, 0), (1, 3))   # tuple of tuples
print(line)               # ((0, 0), (1, 3))
print(len(line))          # 2
t1, t2 = line
(x1, y1), (x2, y2) = line

def distance_to_origin(x, y):
    return math.sqrt(x * x + y * y)  # pythagoras

coordinate = (3, 4)
distance = distance_to_origin(*coordinate)  # unpack operator
print(distance)                             # 5.0
