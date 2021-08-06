
number = input("Give an integer: ")  # user types '5'
print(type(number))   # <class 'str'>
print(number * 4)     # 5555

number = int(number)  # convert to 'int'
print(type(number))   # <class 'int'>
print(number * 4)     # 20

number = input("Give an integer: ")  # user types 'ABC'
number = int(number)  # ValueError: invalid literal for int() with base 10: 'ABC'

while True:
    try:
        number = input("Give an integer:")
        number = int(number)  # ValueError???
        break
    except ValueError:
        print("this is not an integer, try again")
print(number * 4)  # 20
