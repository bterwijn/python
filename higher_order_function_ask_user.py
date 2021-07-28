
def ask_user_for_name_of_less_than_5_characters():
    while True:
        name = input('Give a name of less than 5 characters: ')
        if len(name) < 5:
            break
        print('that is incorrect :(')
    return name

name = ask_user_for_name_of_less_than_5_characters()
print('name:', name)

def ask_user(question, validator_func):  # higher order function
    while True:
        name = input(question)
        if validator_func(name):
            break
        print('that is incorrect :(')
    return name

def has_less_than_5_characters(name):
    return len(name) < 5

name = ask_user('Give a name of less than 5 characters: ', has_less_than_5_characters)
name = ask_user('Give a name of less than 5 characters: ', lambda name: len(name) < 5)
name = ask_user("Give a name that ends with 'n': ", lambda name: name[-1] == 'n')
name = ask_user("Give a name without the letter 'e' and 'a': ",
                lambda name: 'e' not in name and 'a' not in name)
name = ask_user('Give any name: ', lambda name: True)