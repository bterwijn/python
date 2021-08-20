
ints = [3, 5, 8, 6, 2, 5, 8, 6, 7, 3, 1, 5, 6, 5, 2, 8, 4, 6, 5, 1, 5, 8, 3, 9, 8, 2]

int_counts = {}
for i in ints:
    if i not in int_counts:
        int_counts[i] = 0
    int_counts[i] += 1
print(int_counts)  # {3: 3, 5: 6, 8: 5, 6: 4, 2: 3, 7: 1, 1: 2, 4: 1, 9: 1}

int_counts_list = list(int_counts.items())
print(int_counts_list)  # [(3, 3), (5, 6), (8, 5), (6, 4), (2, 3), (7, 1), (1, 2), (4, 1), (9, 1)]

int_counts_list.sort(key=lambda keyvalue: keyvalue[1], reverse=True)
print(int_counts_list)  # [(5, 6), (8, 5), (6, 4), (3, 3), (2, 3), (1, 2), (7, 1), (4, 1), (9, 1)]
