height = 3
width = 4
grid = [ [ (y,x) for x in range(width)] for y in range(height)]
print(grid) # [[(0, 0), (0, 1), (0, 2), (0, 3)], [(1, 0), (1, 1), (1, 2), (1, 3)], [(2, 0), (2, 1), (2, 2), (2, 3)]]
# [
#   [(0, 0), (0, 1), (0, 2), (0, 3)],
#   [(1, 0), (1, 1), (1, 2), (1, 3)],
#   [(2, 0), (2, 1), (2, 2), (2, 3)]
# ]

print( grid[0][3] ) # (0, 3)    y:0, x:3
print( grid[1][2] ) # (1, 2)
grid[1][2] = 888888
grid[2][0] = 999999
# [
#   [(0, 0), (0, 1), (0, 2), (0, 3)],
#   [(1, 0), (1, 1), 888888, (1, 3)],
#   [999999, (2, 1), (2, 2), (2, 3)]
# ]

print( grid[1][2] ) # 88888

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, ' ', end='')
        print()  # prints new-line
        
print_grid(grid)
# (0, 0)  (0, 1)  (0, 2)  (0, 3)  
# (1, 0)  (1, 1)  888888  (1, 3)  
# 999999  (2, 1)  (2, 2)  (2, 3)