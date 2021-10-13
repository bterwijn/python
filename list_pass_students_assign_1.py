'''Schrijf functie get_grade_of_student() die het cijfer returned van
een specifieke student uit een lijst van studenten en corresponderende
lijst van cijfers.
'''

def main():
    students = ["Emma","Tess","Ronald","John","Claudia"]
    grades =   [ 4.5,   6.7,   5.8,     4.9,   7.1]
    print( get_pass_students(students, grades, 5.5) ) # ['Tess', 'Ronald', 'Claudia']

def get_pass_students(students,grades,pass_grade):
    """ Returns a list of studnets taht have a grade highrt or equal to 'pass_grade'.
    Arguments:
    students    -- the list of student names
    grades      -- the correnspondeing list of grades
    pass_grade  -- the passing grade
    """
    pass # add your code here

main()
