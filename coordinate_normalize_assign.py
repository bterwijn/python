import math

def main():
    c1 = Coordinate(1, 2)
    print(c1)  # (1,2)
    c1.scale(2)
    print(c1)  # (2,4)
    print(c1.length())  # 4.47213595499958
    c1.normalize()
    print(c1)  # (0.4472135954999579,0.8944271909999159)

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self, other):
        """ returns a new coordinate that is the sum of coordinates self and other """
        return Coordinate(self.x + other.x, self.y + other.y)

    def __neg__(self):
        """ returns a new coordinate that is the negative of the coordinate """
        return Coordinate(-self.x, -self.y)

    def __sub__(self, other):
        """ returns a new coordinate that is self subtracted by other """
        return self + -other

    def scale(self,scale_factor):
        """ scales the current coordinate by 'scale_factor' (keeping the same direction) """
        # add your code here

    def length(self):
        """ returns the length of the coordinate (distance to origin) """
        # add your code here

    def normalize(self):
        """ scales coordinate so it has length equal to 1 """
        # add your code here
    
main()
