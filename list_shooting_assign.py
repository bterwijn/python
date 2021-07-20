'''Representeer met een tabel (lijst van lijsten) een muur van 20
posities hoog en 40 breed gevuld met het '#' teken. Schiet daar random
gaatjes in door 50 keer een random positie in de muur te overschrijven
met het ' ' teken. Print na elke keer schieten de muur welke er aan
het einde bijvoorbeeld zo uit ziet:

################## # ########### ##### #
########################## ######### ###
########################### ####### ####
#################################### ###
##### ################  ################
######### ############################  
##################################### ##
########################################
######## ###############################
######## ## ############################
### ## ############  ### # ########### #
#### ###################################
############ ##### #####################
############### ################### ####
######## ##### ############ ######## ###
###### ################ ################
########### ##### ################### ##
###################################### #
####### ###### ###  ################ ###
####### ############### ############# # 

hint:

  print(random.randrange(0,10)) # print random een getal van 0 tot 10

'''
import random
import time

def main():
    height = 20
    width = 40
    wall_cell = '#'
    nr_shots = 50
    shot_cell = ' '
    wall = make_wall(width, height, wall_cell)
    for i in range(nr_shots):
        shoot_wall(wall, shot_cell)
        print_wall(wall)
        print() # print new-line to separate walls
        time.sleep(0.1) # sleep for 0.1 seconds
        
def make_wall(width, height, wall_cell):
    """Returns a wall of size 'width' by 'height' filled with value
    'wall_cell'. """
    # add your code here

def shoot_wall(wall, shot_cell):
    """ Shoots a hole in the wall at a rondom position by writing
    'shot_cell' at that position. """
    # add your code here
    
def print_wall(wall):
    """ Prints the values of two dimensional array 'wall'."""
    # add your code here

main()
