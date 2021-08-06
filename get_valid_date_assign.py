
def main():
    year = ask_user_int()
    month = ask_user_int()
    day = ask_user_int()
    print("year:",year,"month:",month,"day:",day)

    # April(4), June(6), September(9), and November(11) have 30 days.
    # Februari(2) has 28 days or 29 days if the year is a leap year.
    # All other months have 31 days.
    #
    # Every year devisible by four is a leap year, except when it is  
    # devisible by 100 and not devisible by 400. For example:
    #  
    #   2004 : leap year
    #   2100 : no leap year
    #   2000 : leap year

def ask_user_int(): # hint: higher order function
    pass

main()
