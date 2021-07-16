n = 3

#           |
# rectangle |       width
#           |   0     1      2
# ----------+---------------------
#        0  | (0, 0)  (1, 0)  (2, 0)
# height 1  | (0, 1)  (1, 1)  (2, 1)
#        2  | (0, 2)  (1, 2)  (2, 2)
#

rectangles = []
for height in range(n):
    for width in range(n):
        rectangles.append((width, height))
print(rectangles)  # [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]

rectangles = [(width, height) for height in range(n) for width in range(n)]
print(rectangles)  # [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
