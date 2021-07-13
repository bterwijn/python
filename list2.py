
grades = [6, 7, 4, 8]
print(grades[1:4])   # [7, 4, 8]
print(grades[1:4:2]) # [7, 8]
print(grades[:2])    # [6, 7]
print(grades[-2:])   # [4, 8]
print(grades[::-1])  # [8, 4, 7, 6]
print(grades)        # [6, 7, 4, 8]

print(4 in grades)        # True
print(grades.index(4))    # 2
print(999 in grades)      # False
#print(grades.index(999)) # ValueError: 999 is not in list

for i in grades:
    print(i,end=" ") # 6 7 4 8

print(list(enumerate(grades))) # [(0, 6), (1, 7), (2, 4), (3, 8)]

for index,value in enumerate(grades):
    print("index:",index,"value:",value)
# index: 0 value: 6
# index: 1 value: 7
# index: 2 value: 4
# index: 3 value: 8
