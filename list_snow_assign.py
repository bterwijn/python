'''Maak een sneeuw-animatie. 
Maak een bord (lijst van lijsten, twee dimensionaal array) gevuld met het '.' 
teken, een lege plek. Schrijf een functie die het bord print. Schrijf een functie 
die tekens op de bovenste regel met een kans van 0.05 vervangt door het '*' teken, 
een sneewvlok. Schrijf een functie die elke sneeuwvlok een positie naar beneden 
verplaatst als daar een '.' teken staat.

hint:

  print(random.random()<0.05) # print True met een kans van 0.05, en anders False
  
'''
import random
import time

def main():
    width = 20
    height = 10
    empty_cell = '.'
    snow_cell = '*'
    snow_chance = 0.05
    board = get_empty_board(width, height, empty_cell)
    print_board(board)
    while True:
        add_random_snow(board, snow_cell, snow_chance)
        print_board(board)
        move_snow(board, empty_cell)
        time.sleep(0.1) # sleep for 0.1 seconds

def get_empty_board(width, height, empty_cell):
    """ Returns a two dimensional array of size 'width' by 'height' filled
    with value 'empty_cell'.
    """
    pass # add your code here

def print_board(board):
    """ Prints the values of two dimensional array 'board'.
    """
    pass # add your code here

def add_random_snow(board, snow_cell, snow_chance):
    """ With a chance of 'snow_chance' adds value 'snow_cell' to the elements
    in the first row of two dimensional array 'board'.
    """
    pass # add your code here

def move_snow(board, empty_cell):
    """ Move any value other then 'empty_cell' one row down in two
    dimensional array 'board' if that spot exists and has value 'empty_cell'.
    """
    pass # add your code here

main()
