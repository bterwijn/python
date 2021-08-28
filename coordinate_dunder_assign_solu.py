
def main():
    c1 = Coordinate(1, 2)
    print(c1)  # (1,2)
    c2 = Coordinate(3, 4)
    print(c2)  # (3,4)

    c3 = c1 + c2
    print(-c3)  # (-4,-6)
    print(c3 - c2)  # (1,2)

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

main()
