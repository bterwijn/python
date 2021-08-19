
my_set = {100, 200, 300}
print(type(my_set))  # <class 'set'>
print(my_set)        # {200, 100, 300}
print(len(my_set))   # 3
my_set = set()       # not "{}", that is used for dictionaries, more later
my_set = set(i * 100 for i in range(1, 4))

my_set.add(400)
print(400 in my_set)      # True
print(500 not in my_set)  # True

for i in my_set:
    print(i, end=' ')  # 200 100 400 300

my_set.discard(100)
print(my_set)       # {200, 400, 300}
my_set.remove(100)  # KeyError: 100
my_set.clear()
