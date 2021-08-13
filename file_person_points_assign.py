import sys
import csv

def main():
    if len(sys.argv) < 2:
        print_help()
        print(f"ERROR: arguments missing.")
        sys.exit(1)

def print_help():
    """ Prints help message """
    print(f"Usage: python {sys.argv[0]} <command> <file>")
    print("Keeps track of points of different people in <file>. Command options:")
    print("  -h/--help            : print this help message")
    print("  -a <name> <points>   : add <points> to person <name>")
    print("  -r <name>            : remove last added points of person <name>")
    print("  -t                   : prints total number of points for each person")
    print("Example:")
    print(f"$ python {sys.argv[0]} -a Mary 2.5 points.csv")
    print(f"$ python {sys.argv[0]} -a John 2   points.csv")
    print(f"$ python {sys.argv[0]} -a John 1.0 points.csv")
    print(f"$ python {sys.argv[0]} -a Mary 2   points.csv")
    print(f"$ python {sys.argv[0]} -r Mary     points.csv")
    print(f"$ python {sys.argv[0]} -t          points.csv")
    print("Mary: 2.5")
    print("John: 3.0")


main()
