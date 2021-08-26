
def main():
    person1 = Person("James", "Taylor", 70.5, 1.71) # object of class Person (variable of type Person)
    person2 = Person("Jack",  "Smith",  67.0, 1.65) # object of class Person
    print(person1.get_full_name())                   # James Taylor
    print(person2.get_full_name())                   # Jack Smith
    print("BMI:", person1.get_body_mass_index())     # BMI: 23.938989774631512
    print("BMI:", person2.get_body_mass_index())     # BMI: 24.609733700642796

class Person:

    def __init__(self, first_name, last_name, weight, height):
        self.name = first_name
        self.surname = last_name
        self.weight = weight
        self.height = height

    def get_full_name(self): # member function, method
        return self.name + ' ' + self.surname   

    def get_body_mass_index(self):
        return self.weight / self.height**2

main()
