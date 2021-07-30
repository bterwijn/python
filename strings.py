
my_string = 'Hello World'
print(my_string)          # Hello World
print(type(my_string))    # <class 'str'>  (immutable)
print(len(my_string))     # 11

print(my_string + my_string)  # Hello WorldHello World
print(my_string * 3)  # Hello WorldHello WorldHello World

print(my_string[4])    # o
print(my_string[-1])   # d
print(my_string[6:])   # World
print(my_string[:5])   # Hello
print(my_string[::-1]) # dlroW olleH

for index, value in enumerate(my_string):
    print("index:", index, "value:", value)
# index: 0 value: H
# index: 1 value: e
# index: 2 value: l
# ...

print('e' in my_string)          # True
print('world' not in my_string)  # True
