
def main():
    person = Person("Carl", "Clarkson", 82.1, 1.89)
    print(person)
    person_list = [Person("James", "Taylor", 70.5, 1.71), Person("Jack", "Smith", 67.0, 1.65)]
    person_list.append(Person("Emma", "Williams", 65.0, 1.69))
    print(person_list)

class Person:

    def __init__(self, first_name, last_name, weight, height):
        self.name = first_name
        self.surname = last_name
        self.weight = weight
        self.height = height

    def get_full_name(self):  # member function, method
        return self.name + ' ' + self.surname

    def get_body_mass_index(self):
        return self.weight / self.height**2

    def __repr__(self):  # dunder/magic method
        return "name:" + self.name + " surname:" + self.surname + \
            " weight:" + str(self.weight) + " height:" + str(self.height)

main()
