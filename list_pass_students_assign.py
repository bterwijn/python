'''Gegeven is een lijst van studenten en een corresponderende lijst van 
cijfers per student. Elke student heeft een aantal cijfer waarbij elk 
cijfer gewogen moet worden met het corresponderende gewicht om het 
gemiddelde cijfer te bepalen. Schrijf functie get_pass_students() die 
een lijst van studenten geeft die een gemiddeld cijfer groter of gelijk 
aan de 'pass_grade' hebben.
'''

def main():
    students = ['Jennifer',        'Daniel',          'Patricia',         'Anthony']
    grades =  [[1.01, 5.44, 7.81], [3.2, 3.93, 8.83], [6.12, 3.11, 6.85], [4.71, 8.23, 5.03]]
    weights =  [0.7,  1.1,  1.5]
    pass_grade = 5.5
    print(get_pass_students(students, grades, weights, pass_grade)) # ['Jennifer', 'Daniel', 'Anthony']

def get_pass_students(students, grades, weights, pass_grade):
    """Returns a list of students that have an average grade higher or
    equal to 'pass_grade'. The 'grades' contain the correspoding grades for
    each student that have to be weigted by the corresponding 'weights'."""
    pass_students = []
    return pass_students

main()
