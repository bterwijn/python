'''Schrijf functie get_pass_students() die een lijst van studenten
returned die een cijfer hoger of gelijk aan pass_grade hebben.
'''

def main():
    students = ["Emma","Tess","Ronald","John","Claudia"]
    grades =   [ 4.5,   6.7,   5.8,     4.9,   7.1]
    print( get_pass_students(students,grades,5.5) ) # ['Tess', 'Ronald', 'Claudia']

def get_pass_students(students,grades,pass_grade):
    """ Returns a list of students that have a grade higher or equal to 'pass_grade'.
    Arguments:
    students   -- the list of student names
    grades     -- the corrensponding list of grades
    pass_grade -- the passing grade
    """
    pass_students=[]
    for index,grade in enumerate(grades):
        if grade>=pass_grade:
            pass_students.append(students[index])
    return pass_students

main()
