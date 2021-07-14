n = 3

my_list = []
for i in range(n):
    my_list.append(i)
print(my_list)  # [0, 1, 2]

my_list = list(range(n))
print(my_list)  # [0, 1, 2]

my_list = [i for i in range(n)]  # list comprehension
print(my_list)  # [0, 1, 2]

square_surfaces = [i**2 for i in range(n)]  # surface of squares with length 0 up to n-1
print(square_surfaces)  # [0, 1, 4]
