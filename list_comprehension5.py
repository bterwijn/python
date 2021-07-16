n = 3
#           |
# rectangle |       width
#           |   0     1      2
# ----------+---------------------
#        0  | (0, 0)  (0, 1)  (0, 2)  
# height 1  | (1, 0)  (1, 1)  (1, 2)  
#        2  | (2, 0)  (2, 1)  (2, 2)
#

rectangles = []
for height in range(n):
    for width in range(n):
        if (height <= width):
            rectangles.append( (height, width) )
print(rectangles)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

rectangles = [ (height, width) for height in range(n) for width in range(n) if (height <= width)]
print(rectangles)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
