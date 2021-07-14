n = 3

square_surfaces = [length**2 for length in range(n)]  # surface of squares with length 0 up to n-1
print(square_surfaces)  # [0, 1, 4]

rectangle_surfaces = [width * height for width in range(n) for height in range(n)]
print(rectangle_surfaces)  # [0, 0, 0, 0, 1, 2, 0, 2, 4]

rectangle_surfaces = [(width, height, width * height)
                      for width in range(n)
                      for height in range(n)]
print(rectangle_surfaces)
# [(0, 0, 0), (0, 1, 0), (0, 2, 0), (1, 0, 0), (1, 1, 1), (1, 2, 2), (2, 0, 0), (2, 1, 2), (2, 2, 4)]

rectangle_surfaces = [(width, height, width * height)
                      for width in range(n)
                      for height in range(n)
                      if height <= width]
print(rectangle_surfaces)  # [(0, 0, 0), (1, 0, 0), (1, 1, 1), (2, 0, 0), (2, 1, 2), (2, 2, 4)]

rectangle_surfaces = [(width, height, width * height)
                      for width in range(n)
                      for height in range(width+1)]
print(rectangle_surfaces)  # [(0, 0, 0), (1, 0, 0), (1, 1, 1), (2, 0, 0), (2, 1, 2), (2, 2, 4)]
