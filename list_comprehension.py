n = 3

my_list = []
for i in range(n):
    my_list.append(i)
print(my_list)  # [0, 1, 2]

my_list = [0, 1, 2]
my_list = [i for i in range(n)]
print(my_list)  # [0, 1, 2]
