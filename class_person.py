
def main():
    person = {"name": "James", "surname": "Taylor", "weight": 70.5, "height": 1.71}
    print(type(person))                                         # <class 'dict'>
    print(person["name"], person["surname"], person["weight"])  # James Taylor 70.5

    person = Person("James", "Taylor", 70.5, 1.71)     # object of class Person
    print(type(person))                                # <class '__main__.Person'>
    print(person.name, person.surname, person.weight)  # James Taylor 70.5

class Person:

    def __init__(self, first_name, last_name, weight, height):
        self.name = first_name  # initialize member variables
        self.surname = last_name
        self.weight = weight
        self.height = height 
        # no 'return self'

main()