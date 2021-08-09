import csv

with open('test.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([0, 'John, Clark and Thomas', 12])
    csv_writer.writerow([1, 'Mary Smith', 14])
    csv_writer.writerow([2, 'Peter Brown', 11])

total = 0
with open('test.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
        try:
            total += float(row[2])
        except ValueError:
            print(f"'{row[2]}' is not a float on line: {row}")
# ['0', 'John, Clark and Thomas', '12']
# ['1', 'Mary Smith', '14']
# ['2', 'Peter Brown', '11']
print(total)  # 37.0
