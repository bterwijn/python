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
    for index, name in enumerate(students):
        grade = compute_grade(grades[index], weights)
        if grade >= pass_grade:
            pass_students.append(name)
    return pass_students    
    return [name for index, name in enumerate(students)
            if compute_grade(grades[index], weights) >= pass_grade] # or use a list comprehension
            
def compute_grade(grades, weights):
    """ Computes the average of 'grades' weighted by the corresponding 'weights'. """
    sum_grade = 0
    sum_weight = 0
    for index, grade in enumerate(grades):
        sum_grade += grade * weights[index]
        sum_weight += weights[index]
    return sum_grade / sum_weight

main()
