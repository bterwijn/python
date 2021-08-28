
def main():
    person1 = Person("James", "Taylor", 70.5, 1.71)
    person1.loose_weight(0.4)
    print(person1)  # name:James surname:Taylor weight:70.1 height:1.71
    person2 = Person("Jack", "Smith", 67.0, 1.65)
    print(person1.is_taller_than(person2))  # True

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

    def loose_weight(self, weight_loss):  # method changes object
        self.weight -= weight_loss

    def is_taller_than(self, other):  # compares peron 'self' and person 'other'
        return self.height > other.height

main()
