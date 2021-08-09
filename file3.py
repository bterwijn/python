import os

filename=os.path.join('directory','subdir','log.txt')
print(filename) # Linux/Mac:  directory/subdir/log.txt
                # Windows:    directory\subdir\log.txt
try:
    with open(filename, 'w') as file:
        file.write('0 John 12\n')
        file.write('1 Mary 14\n')
        file.write('2 Peter 11\n')
except FileNotFoundError:
    print(f"ERROR: Couldn't open file '{filename}'")
