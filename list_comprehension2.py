n = 3

my_list = []
for i in range(n):
    my_list.append(i**2)
print(my_list)  # [0, 1, 4]

my_list = [i**2 for i in range(n)]
print(my_list)  # [0, 1, 4]
