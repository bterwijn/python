
with open('test.txt', 'w') as file:
    file.write('0    John        12\n')
    file.write('  1   Mary        14\n')
    file.write('2       Peter    11   \n')

total = 0
with open('test.txt', 'r') as file:
    for line in file:
        elements = line.split()
        print(elements)
        try:
            total += float(elements[2])
        except ValueError:
            print("'", elements[2], "' is not a float")
# ['0', 'John', '12']
# ['1', 'Mary', '14']
# ['2', 'Peter', '11']
print(total)  # 37.0
