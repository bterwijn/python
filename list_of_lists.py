height = 3
table = [ [0, 0, 0, 0] for row in range(height)]
print(table) # [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]

width = 4
table = [ [0 for column in range(width)] for row in range(height)]

table[0][1] = 99
table[1][2] = 77
print(table[1][2]) # 77
print(table) # [ [0, 99, 0, 0], [0, 0, 77, 0], [0, 0, 0, 0] ]

def print_table(table):
    for row in table:
        for cell in row:
            print(cell, ' ', end='')
        print() # prints new-line
            
print_table(table)
#  0 99  0  0  
#  0  0 77  0  
#  0  0  0  0 

print("table height:", len(table) )   # 3
print("table width:", len(table[0]) ) # 4
