import sys
import csv

def main():
    if len(sys.argv) < 2:
        print_help()
        print(f"ERROR: arguments missing.")
        sys.exit(1)
    command = sys.argv[1]
    if command == '-h' or command == '--help':
        print_help()
    elif command == '-a':
        if len(sys.argv) < 5:
            print(f"ERROR: '-a' arguments missing.")
            sys.exit(1)
        name = sys.argv[2]
        try:
            points = float(sys.argv[3])
        except ValueError:
            print(f"ERROR: points have to be a float instead of '{sys.argv[4]}'.")
        filename = sys.argv[4]
        add_points(filename, name, points)
    elif command == '-r':
        if len(sys.argv) < 4:
            print("ERROR: '-r' arguments missing.")
            sys.exit(1)
        name = sys.argv[2]
        filename = sys.argv[3]
        remove_last_points(filename, name)
    elif command == '-t':
        if len(sys.argv) < 3:
            print("ERROR: '-t' arguments missing.")
            sys.exit(1)
        filename = sys.argv[2]
        print_totals(filename)
    else:
        print(f"ERROR: Invalid command '{command}'.")
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

def add_points(filename, name, points):
    """ Add 'points' to 'name' in file 'filename'  """
    person_points_list = read_file(filename)
    found = False
    for person_points in person_points_list:
        if len(person_points)>0 and name == person_points[0]:
            person_points.append(points)
            found = True
    if not found:
        person_points_list.append([name, points])
    write_file(filename, person_points_list)

def remove_last_points(filename, name):
    """ Remove last 'points' of 'name' in file 'filename' """
    person_points_list = read_file(filename)
    found = False
    for person_points in person_points_list:
        if len(person_points)>0 and name == person_points[0] and len(person_points) > 1:
            person_points.pop()
            found = True
    if not found:
        print(f"Couldn't remove points from person '{name}'.")
    write_file(filename, person_points_list)

def print_totals(filename):
    """ Print totals of all people in file 'filename'  """
    person_points_list = read_file(filename)
    for person_points in person_points_list:
        print_person_points_total(person_points)

def print_person_points_total(person_points):
    """ Prints the person (first list element) and it totals points (other list elements) """
    total_points = 0
    for value in person_points[1:]:
        total_points += float(value)
    print(f"{person_points[0]}: {total_points}")

def read_file(filename):
    """ Reads the file and returns a list of list where each list begins with a name
     that is followed by the points of that person """
    person_points_list = []
    try:
        with open(filename, 'r', newline='') as file: # newline='' required on Windows to avoid empty lines
            csv_reader = csv.reader(file)
            for row in csv_reader:
                person_points_list.append(row)
    except FileNotFoundError:
        pass
    return person_points_list

def write_file(filename, person_points_list):
    """ Writes a list of list (where each list begins with a name
     that is followed by the points) to file 'filename' """
    try:
        with open(filename, 'w', newline='') as file: # newline='' required on Windows to avoid empty lines
            csv_writer = csv.writer(file)
            csv_writer.writerows(person_points_list)
    except FileNotFoundError:
        print(f"ERROR: Couldn't write to file '{filename}'.")
        sys.exit(1)

main()
