
file1 = open('test.txt', 'a') # 'a' for append at the end
file1.write('0 John 12\n')
file1.write('1 Mary 14\n')
file1.write('2 Peter 11\n')
file1.close() # flushes, content is guarenteed to be on the disk

file2 = open('test.txt', 'r')
for line in file2:
    print(line,end='')
file2.close()
