'''Sorteer de coordinaten (3,5), (2,3), (5,4), (6,2) op afstand tot (4,3). '''

def main():
    coordinates = [(3,5), (2,3), (5,4), (6,2)]
    sort_by_distance_to((4,3), coordinates)
    print(coordinates) # [(5,4), (2,3), (3,5), (6,2)]

def sort_by_distance_to(coord, coordinates):
    """ Sorts the coordinates by distance to coord. """
    # add your code here

main()
