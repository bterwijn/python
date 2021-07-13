'''Schrijf functie get_grade_of_student() die het cijfer returned van
een specifieke student uit een lijst van studenten en corresponderende
lijst van cijfers.
'''

def main():
    students = ["Emma","Tess","Ronald","John","Claudia"]
    grades =   [ 4.5,   6.7,   5.8,     4.9,   7.1]
    while True:
        name=input("Which student's grade would you like to see? ")
        grade,valid = get_grade_of_student(students,grades,name)
        if valid:
            print("student",name,"has grade:",grade)
        else:
            print("student",name,"not found")

def get_grade_of_student(students,grades,name):
    """ Returns (grade,valid) where grade is the grade in 'grades' at the 
        same index as 'name' is in 'students'. Valid is True if 'name' is in 
        'students' and False otherwise."""
    grade=0
    valid=False
    if name in students:
        index = students.index(name)
        grade = grades[index]
        valid = True
    return (grade,valid)    

main()
