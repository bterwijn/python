
def main():
    menu = Menu()
    persons = menu.create_persons()
    menu.print_persons_by_height(persons)

class Menu:

    def __init__(self):
        pass

    def create_persons(self):
        persons = Persons()
        persons.add_person(Person("James", "Taylor", 70.5, 1.71, Date(5, 1, 1994)))
        persons.add_person(Person("Emma", "Williams", 65.0, 1.69, Date(16, 11, 1989)))
        persons.add_person(Person("Jack", "Smith", 67.0, 1.65, Date(23, 4, 2001)))
        return persons

    def print_persons_by_height(self, persons):
        step = 10
        for height in range(150, 190, step):
            min_height = height / 100
            max_height = (height + step) / 100
            print("height:", min_height, "-", max_height)
            print(persons.get_persons_by_height(min_height, max_height))

class Persons:

    def __init__(self):
        self._persons = []

    def __repr__(self):
        return f"{self._persons}"

    def add_person(self, person):
        self._persons.append(person)

    def get_persons_by_height(self, min_height, max_height):
        result = Persons()
        for person in self._persons:
            if person.height >= min_height and person.height < max_height:
                result.add_person(person)
        return result

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
        self._day = day
        self._month = month
        self._year = year
        self.check_valid()

    def check_valid(self):
        if not is_valid_month(self._month):
            raise ValueError(f'Not a valid month: {self}')
        if not is_valid_day(self._day, self._year, self._month):
            raise ValueError(f'Not a valid day: {self}')

    def __repr__(self):
        return f"{self._day:02d}-{self._month:02d}-{self._year}"

    def year_difference(self, other):
        result = other._year - self._year
        if other._month < self._month:
            result -= 1
        elif other._month == self._month and other._day < self._day:
            result -= 1
        return result

    def set_year(self, year):
        self._year = year
        self.check_valid()

# from get_valid_date_assign_solu.py
def is_valid_month(month):
    """ Returns True when 'month' has a valid month value (1-12), False otherwise """
    return month >= 1 and month <= 12

def is_valid_day(day, year, month):
    """ Returns True when 'day' has a valid day value in month 'month' of year 'year',
        False otherwise """
    return day >= 1 and day <= compute_days_in_month(month, year)

def compute_days_in_month(month, year):
    """ Returns the number of days in month 'month' of year 'year' """
    if month in [4, 6, 9, 11]:  # April(4), June(6), September(9), and November(11) have 30 days.
        return 30
    if month == 2:  # Februari(2) has 28 days or 29 days if the year is a leap year.
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31  # All other months have 31 days.

def is_leap_year(year):
    """ Returns True if 'year' is a leap year """
    leap_year = False
    if year % 4 == 0:                            # Every year devisible by four is a leap year
        leap_year = True
        if year % 100 == 0 and year % 400 != 0:  # except when it is devisible by 100 and not
            leap_year = False                    # devisible by 400
    return leap_year


main()
