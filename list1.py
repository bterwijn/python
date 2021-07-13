grades = [6, 7, 4, 8] # often homogenous
print(type(grades))   # <class 'list'>
print(len(grades))    # 4

print(grades[0])      # 6
print(grades[3])      # 8
print(grades[-1])     # 8
print(grades[-4])     # 6
# print(grades[ 4])  # IndexError: list index out of range
# print(grades[-5])  # IndexError: list index out of range

grades.append(9)        # mutable
grades[0]=3             
print(grades)           # [3, 7, 4, 8, 9]
print(grades + [7, 5])  # [3, 7, 4, 8, 9, 7, 5]
print(grades)           # [3, 7, 4, 8, 9]
grades += [7, 5]        # grades = grades + [7, 5]
print(grades)           # [3, 7, 4, 8, 9, 7, 5]
print(grades*2)         # [3, 7, 4, 8, 9, 7, 5, 3, 7, 4, 8, 9, 7, 5]

grades.insert(1, 10)
print(grades)           # [3, 10, 7, 4, 8, 9, 7, 5]

grades.pop()
print(grades)           # [3, 10, 7, 4, 8, 9, 7]
grades.pop(1)
print(grades)           # [3, 7, 4, 8, 9, 7]
