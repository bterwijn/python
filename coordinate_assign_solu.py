
def main():
    c1 = Coordinate(1, 2)
    print(c1)  # (1,2)
    c2 = Coordinate(3, 4)
    print(c2)  # (3,4)

    c3 = c1.add(c2)
    print(c3.negative()) # (-4,-6)
    print(c3.subtract(c2)) # (1,2)

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def add(self, other):
        """ returns a new coordinate that is the sum of coordinates self and other """
        return Coordinate(self.x + other.x, self.y + other.y)

    def negative(self):
        """ returns a new coordinate that is the negative of the coordinate """
        return Coordinate(-self.x, -self.y)

    def subtract(self, other):
        """ returns a new coordinate that is self subtracted by other """
        return self.add(other.negative())

main()
