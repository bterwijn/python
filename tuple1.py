x = 4  # represent a coordinate
y = 7

coordinate = (x, y)
print(type(coordinate))  # <class 'tuple'>
print(coordinate)        # (4, 7)
print(coordinate[0])     # 4
print(coordinate[1])     # 7
a, b = coordinate        # tuple unpack
print("a:", a, "b:", b)  # a: 4 b: 7

def add_coordinates(coordinate1, coordinate2):
    x1, y1 = coordinate1
    x2, y2 = coordinate2
    return (x1 + x2, y1 + y2)

result = add_coordinates((4, 7), (2, 1))
print(result)  # (6, 8)

coordinate = (1, 2, 3)
print(coordinate)       # (1, 2, 3)
print(len(coordinate))  # 3

for i in coordinate:
    print(i)  # 1'\n'2'\n'3'\n'

coordinate[0] = 100  # TypeError: 'tuple' object does not support item assignment
                     # tuple: immutable type
