
def ask_user_for_int(question):
    return int(input(question))

def divide_two_ints():
    while True:
        try:
            int1 = ask_user_for_int("Type int1: ")
            break
        except ValueError:
            print("please try again for int1")
    int2 = ask_user_for_int("Type int2: ")
    return int1 / int2

def main():
    while True:
        try:
            print(divide_two_ints())
            break
        except ValueError:
            print("please try again for int1 and int2")

main()
