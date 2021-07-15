'''Maak een bord (lijst van lijsten, twee dimensionaal array) van 40
hoog en 20 breed gevuld met het '#' teken. Schiet daar random gaatjes
in door 50 random cellen in het bord te overschrijven met het ' ' teken.
Print vervolgens het bord.

hint:

  print(random.randint(0,10)) # print random een getal van 0 t/m 10

'''
import random
import time

def main():
    width = 40
    height = 20
    board_cell = '#'
    nr_shots = 50
    shot_cell = ' '
    board = build_board(width, height, board_cell)
    for i in range(nr_shots):
        shoot_board(board, shot_cell)
        print_board(board)
        time.sleep(0.1)  # sleep for 0.1 seconds
        
def build_board(width, height, board_cell):
    """ Returns a two dimensional array of size 'width' by 'height' filled
    with value 'board_cell'."""
    return [[board_cell for x in range(width)] for y in range(height)]

def build_board_alternative_1(width, height, board_cell):
    board = []
    for y in range(height):
        board.append([board_cell for i in range(width)])
    return board

def build_board_alternative_2(width, height, board_cell):
    board = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(board_cell)
        board.append(row)
    return board

def shoot_board(board, shot_cell):
    """ Shoots a hole in the board at a rondom position by writing
    'shot_cell' at that position. """
    height = len(board)
    width = len(board[0])
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    board[y][x] = shot_cell
    
def print_board(board):
    """ Prints the values of two dimensional array 'board'.
    """
    print()  # empty line as boards separator
    for row in board:
        for cell in row:
            print(cell, end='')
        print()

main()
