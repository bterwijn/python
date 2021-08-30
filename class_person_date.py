
def main():
    date = Date(5, 1, 1994)
    person = Person("James", "Taylor", 70.5, 1.71, date)
    print(person)
    today = Date(29, 2, 2020)
    print("ages:", person.get_age(today))

class Person:

    def __init__(self, first_name, last_name, weight, height, birth_date):
        self.name = first_name
        self.surname = last_name
        self.weight = weight
        self.height = height
        self.birth_date = birth_date

    def __repr__(self):
        return f"name:{self.name} surname:{self.surname} weight:{self.weight} " \
            f"height:{self.height} birth_date:{self.birth_date}"

    def get_name(self):
        return f"{self.name} {self.surname}"

    def get_body_mass_index(self):
        return self.weight / self.height**2

    def get_age(self, current_date):
        return self.birth_date.year_difference(current_date)

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __repr__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

    def year_difference(self, other):
        result = other.year - self.year
        if other.month < self.month:
            result -= 1
        elif other.month == self.month and other.day < self.day:
            result -= 1
        return result

main()
