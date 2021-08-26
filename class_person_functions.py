
def main():
    person1 = Person("James", "Taylor", 70.5, 1.71) # object of class Person (variable of type Person)
    person2 = Person("Jack",  "Smith",  67.0, 1.65) # object of class Person
    print(get_full_name(person1))                   # James Taylor
    print(get_full_name(person2))                   # Jack Smith
    print("BMI:", get_body_mass_index(person1))     # BMI: 23.938989774631512
    print("BMI:", get_body_mass_index(person2))     # BMI: 24.609733700642796

class Person:

    def __init__(self, first_name, last_name, weight, height):
        self.name = first_name
        self.surname = last_name
        self.weight = weight
        self.height = height

def get_full_name(person):
    return person.name + ' ' + person.surname

def get_body_mass_index(person):
    return person.weight / person.height**2

main()
