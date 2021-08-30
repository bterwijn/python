import numpy  # pip install numpy
import datetime

def main():
    c1 = numpy.array([1, 2])
    c2 = numpy.array([3, 4])
    c3 = c2 - c1
    print(c3)  # [2 2]
    print("length:", numpy.linalg.norm(c3))  # length: 2.8284271247461903

    now = datetime.datetime.now()
    print("now:", now)
    try:
        birthday = datetime.datetime(1998, 5, 17)
    except ValueError:
        pass
    print("birthday:", birthday)
    print("seconds in between:", (now - birthday).total_seconds())

main()
