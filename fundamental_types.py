
print(type(123))            # <class 'int'>   (integer, whole numbers)
print(type(4.46))           # <class 'float'> (floating point numbers)
print(type(1 > 2))          # <class 'bool'>  (boolean: True/False)
print(type('Hello World'))  # <class 'str'>   (string)

print(-2**200)         # -1606938044258990275541962092341162602522202993782792835301376
print(15 / 11)         # 1.3636363636363635
print(15 // 11)        # 1
print(-15 // 11)       # -2
print((15 / 11) * 11)  # 14.999999999999998

v1 = 11
v2 = 22
print(type(v1))  # <class 'int'>
print(v1 + v2)   # 33

v1 = '11'
v2 = '22'
print(type(v1))  # <class 'str'>  (dynamic typing)
print(v1 + v2)   # '1122'

v1 = 11
v2 = '22'
print(v1 + v2)   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
