'''Maak een sneeuw-animatie. Representeer hiervoor met een tabel
(lijst van lijsten) een stuk luchtruim van 10 posities hoog en 20
breed gevuld met het '.' teken, een lege plek. Schrijf:
- een functie die het luchtruim aanmaakt
- een functie die het luchtruim print
- een functie die elk teken op de bovenste regel van het luchtruim met 
een kans van 0.05 vervangt door het '*' teken, een sneewvlok
- een functie die elke sneeuwvlok een positie naar beneden verplaatst 
als daar een '.' teken staat

Gebruik deze functies om een sneeuw-animatie te maken. 

hint:

  print(random.random() < 0.05) # print 'True' met een kans van 0.05, en anders 'False'

'''
import random
import time

def main():
    width = 20
    height = 10
    empty_cell = '.'
    snow_cell = '*'
    snow_chance = 0.05
    sky = make_empty_sky(width, height, empty_cell)
    while True:
        add_random_snow(sky, snow_cell, snow_chance)
        print_sky(sky)
        print() # print new-line to separate skies
        move_snow(sky, empty_cell)
        time.sleep(0.1) # sleep for 0.1 seconds

def make_empty_sky(width, height, empty_cell):
    """ Returns a piece of sky of 'width' by 'height' filled
    with value 'empty_cell'. """
    return [[empty_cell for col in range(width)] for row in range(height)]

def print_sky(sky):
    """ Prints the 'sky'. """
    for row in sky:
        for cell in row:
            print(cell, end='')
        print()

def add_random_snow(sky, snow_cell, snow_chance):
    """ With a chance of 'snow_chance' adds value 'snow_cell' to each column
    of the first row of 'sky'. """
    width = len(sky[0])
    for column_index in range(width):
        if random.random() < snow_chance:
            sky[0][column_index] = snow_cell

def move_snow(sky, empty_cell):
    """ Move any value other then 'empty_cell' one row down in 'sky' if that 
    spot exists and has value 'empty_cell'. """
    height = len(sky)
    width = len(sky[0])
    for row_index in reversed(range(height - 1)):
        for column_index in range(width):
            if sky[row_index][column_index] != empty_cell:
                next_row_index = row_index + 1
                if sky[next_row_index][column_index] == empty_cell:
                    sky[next_row_index][column_index] = sky[row_index][column_index]
                    sky[row_index][column_index] = empty_cell

main()
