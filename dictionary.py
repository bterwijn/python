my_dict = {'Betty': 21, 'Sarah': 10, 'Mark': 19, 'Sandra': 18}
print(type(my_dict))  # <class 'dict'>, not sorted
print(len(my_dict))   # 4

print(my_dict['Sandra'])  # 18
my_dict['Sandra'] = 99    # changes value of existing key
my_dict['John'] = 50      # adds value of a new key
print(my_dict)            # {'Sarah': 10, 'Mark': 19, 'Betty': 21, 'Sandra': 99, 'John': 50}

my_list = [21, 10, 19, 18]
print(my_list[3])  # 18
my_list[3] = 99

# print(my_dict['Richard'])  # KeyError: 'Richard'
if 'Richard' in my_dict:
    print(my_dict['Richard'])

for i in my_dict:
    print(i, end=' ')  # Betty Sarah Mark Sandra John

for key, value in my_dict.items():
    print(key, ':', value, sep='', end=' ')  # Betty:21 Sarah:10 Mark:19 Sandra:99 John:50

if 'Mark' in my_dict:
    del my_dict['Mark']

my_dict.clear()
my_dict = {}
