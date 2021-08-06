import sys

def main():
    if len(sys.argv) < 2:
        print_help()
        print("ERROR: Operator missing.")
        sys.exit(1)  # exit with error
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_help()
        sys.exit(0)  # exit without error
    operator = sys.argv[1]
    arguments = sys.argv[2:]
    if operator == 'add':
        print(operate(lambda a, b: a + b, 0, arguments))
    elif operator == 'mult':
        print(operate(lambda a, b: a * b, 1, arguments))
    else:
        print("ERROR: Invalid Operator '", operator, "' either use 'add' or 'mult'.")
        sys.exit(1)
    sys.exit(0)  # exit without error

def print_help():
    print("Usage: python", sys.argv[0], " <Operator> [<float> ...]")
    print("Applies the Operator to all the float arguments and prints the result.")
    print("Operator can be 'add' for addition, or 'mult' for multiplication.")
    print("Examples: $ python", sys.argv[0], "add 2 1.5")
    print("          $ 3.5")
    print("          $ python", sys.argv[0], "mult 2 1.5 3")
    print("          $ 9")

def operate(operator, result, arguments):
    """ Applies 'operator' to all 'arguments' after conversion to float starting  
        with 'start_value' and returns the result. """
    for argument in arguments:
        try:
            float_argument = float(argument)
        except ValueError:
            print("ERROR: Could not convert '",argument,"' to float.")
            sys.exit(1)
        result = operator(result, float_argument)
    return result

main()
