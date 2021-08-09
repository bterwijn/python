
# previously: file1 = open('test.txt', 'w')
with open('test.txt', 'w') as file1: # file gets closed automatically
    file1.write('0 John 12\n')
    file1.write('1 Mary 14\n')
    file1.write('2 Peter 11\n')

with open('test.txt', 'r') as file2: # file gets closed automatically
    for line in file2:
        print(line,end='')
