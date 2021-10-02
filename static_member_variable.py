import random

def main():
    test()
    
def test():
    p1 = Person("Jennifer")
    print(p1)
    p2 = Person("Daniel")
    print(p2)

class Person:
    id = 0                               # id         : 'static member' or 'class' variable

    def __init__(self, name):
        self.name = name                 # self.name  : 'member' or 'instance' variable
        h = random.uniform(1.5, 2)       # h          : 'local' variable
        self.height = h                  # self.height: 'member' or 'instance' variable
        self.id = Person.id
        Person.id += 1

    def __repr__(self):
        return f"id:{self.id} name:{self.name} height:{self.height}"

main()
