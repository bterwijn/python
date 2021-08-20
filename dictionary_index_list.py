
ints = [3, 5, 8, 6, 2, 5, 8, 6, 7, 3, 1, 5]

int_indices = {}
for index, value in enumerate(ints):
    if value not in int_indices:
        int_indices[value] = []
    int_indices[value].append(index)
print(int_indices)  # {3: [0, 9], 5: [1, 5, 11], 8: [2, 6], 6: [3, 7], 2: [4], 7: [8], 1: [10]}

int_indices_list = list(int_indices.items())
int_indices_list.sort()
print(int_indices_list)  # [(1, [10]), (2, [4]), (3, [0, 9]), (5, [1, 5, 11]), (6, [3, 7]), (7, [8]), (8, [2, 6])]
