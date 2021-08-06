import sys

def main():
    if len(sys.argv) < 2:
        print_help()
        print("ERROR: Operator missing.")
        sys.exit(1)  # exit with error
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_help()
        sys.exit(0)  # exit without error
    # add your code here
    sys.exit(0)  # exit without error

def print_help():
    print("Usage: python", sys.argv[0], "<Operator> [<float> ...]")
    print("Applies the Operator to all the float arguments and prints the result.")
    print("Operator can be 'add' for addition, or 'mult' for multiplication.")
    print("Examples: $ python", sys.argv[0], "add 2 1.5")
    print("          $ 3.5")
    print("          $ python", sys.argv[0], "mult 2 1.5 3")
    print("          $ 9")

# add your functions here

main()
