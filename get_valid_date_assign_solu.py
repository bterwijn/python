
def main():
    year = ask_user_int("Which year? ", lambda year: True)
    month = ask_user_int("Which month? (1-12)", is_valid_month)
    day = ask_user_int("Which day of the month? ", lambda day: is_valid_day(day, year, month))
    print("year:", year, "month:", month, "day:", day)

def ask_user_int(question, validator_function):
    """ Keeps asking the user a 'question' until the answer is an integer that is validated
        by the 'validator_function'. The answer is returned. """
    while True:
        try:
            user_int = int(input(question))
            if validator_function(user_int):
                break
            else:
                print("invalid, not a valid value")
        except ValueError:
            print("invalid, not an integer")
    return user_int

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
