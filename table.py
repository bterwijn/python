list = [0, 0, 0, 0]
list[2] = 99
print(list)    # [0, 0, 99, 0]
print(list[2]) # 99


table = [
           [0,  0,  0,  0],
           [0,  0,  0,  0],
           [0,  0,  0,  0]
        ]
table[0][1] = 99
table[1][2] = 77
print(table)
# [
#   [0, 99,  0,  0],
#   [0,  0, 77,  0],
#   [0,  0,  0,  0]
# ]
print(table[1][2]) # 77
