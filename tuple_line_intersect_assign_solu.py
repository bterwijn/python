'''Schrijf de functie line_intersection() die geven 2 lijnen het
coordinaat van het snijpunt van de lijnen returned.
'''

def main():
    line1 = (1, -2)   # y = 1*x -2
    line2 = (-2, 10)  # y = -2*x +10
    print(line_intersection_point(line1, line2))
    line3 = (1, 5)    # y = 1*x +5
    print(line_intersection_point(line1, line3))

def line_intersection_point(line1, line2):
    """
    Returns the intersection point of two lines.
    Returns tuple ((x,y),valid) where (x,y) is the coordinate of the intersection point and 
    'valid' is a boolean indicating the intersection point is valid or not.
    """
    a1, b1 = line1
    a2, b2 = line2
    # === doing some line intersection math:
    # a1*x+b1 = a2*x+b2
    # (a1-a2)*x = b2-b1
    # x = (b2-b1) / (a1-a2)
    # y = a1*x + b1
    divisor = a1 - a2
    if divisor == 0:
        x = 0
        y = 0
        valid = False
    else:
        x = (b2 - b1) / divisor
        y = a1 * x + b1
        valid = True        
    return ((x, y), valid)

main()
