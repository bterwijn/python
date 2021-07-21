'''Sorteer de coordinaten (3,5), (2,3), (5,4), (6,2) op afstand tot (4,3). '''

import math

def main():
    coordinates = [(3,5), (2,3), (5,4), (6,2)]
    sort_by_distance_to((4,3), coordinates)
    print(coordinates) # [(5,4), (2,3), (3,5), (6,2)]

def sort_by_distance_to(coord, coordinates):
    """ Sorts the coordinates by distance to coord. """
    coordinates.sort(key=lambda c: distance_between_coordinates(coord,c))

def distance_between_coordinates(c1,c2):
    """ Returns the distance between coordindate c1 and c2. """
    dx = c1[0] - c2[0]
    dy = c1[1] - c2[1]
    return math.sqrt(dx**2 + dy**2) # pythagoras

main()
