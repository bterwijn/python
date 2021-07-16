import math
n = 3

my_list = []
for i in range(n):
    my_list.append(math.sqrt(i))
print(my_list)  # [0, 1, 1.414]

my_list = [math.sqrt(i) for i in range(n)]
print(my_list)  # [0, 1, 1.414]
