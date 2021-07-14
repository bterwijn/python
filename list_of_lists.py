height = 3
width = 4
board = [ [(x, y) for x in range(width)] for y in range(height)]
print(board)  # [  [(0, 0), (1, 0), (2, 0), (3, 0)],
              #    [(0, 1), (1, 1), (2, 1), (3, 1)],
              #    [(0, 2), (1, 2), (2, 2), (3, 2)]   ]

def print_board(board):
    for line in board:
        for element in line:
            print(element, ' ', end='')
        print()  # prints new-line

print_board(board)
# (0, 0)  (1, 0)  (2, 0)  (3, 0)
# (0, 1)  (1, 1)  (2, 1)  (3, 1)
# (0, 2)  (1, 2)  (2, 2)  (3, 2)

board[0][0] = 'XXXXXX'
board[1][3] = '******'
print_board(board)
# XXXXXX  (1, 0)  (2, 0)  (3, 0)
# (0, 1)  (1, 1)  (2, 1)  ******
# (0, 2)  (1, 2)  (2, 2)  (3, 2)
