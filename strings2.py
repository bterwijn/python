print("Abcd".upper())     # ABCD
print("Abcd".lower())     # abcd
print("Abcd".center(20))  # '        Abcd        '

print("yes no yes XXyesXX".count("yes"))  # 3

print("yes no yes XXyesXX".find("yes"))     # 0
print("yes no yes XXyesXX".find("yes", 1))  # 7
print("yes no yes XXyesXX".rfind("yes"))    # 13

print("yes no yes XXyesXX".replace("yes", "NO", 2))  # NO no NO XXyesXX

print("     yes    no    ".strip())      # 'yes    no'
print("__+__yes_+__no__++".strip("_+"))  # 'yes_+__no'

print("first    second  third".split())     # ['first', 'second', 'third']
print("first,second,third".split(','))      # ['first', 'second', 'third']
print(",".join(['first', 'second', 'third']))  # 'first,second,third'

print("abc".islower())    # True
print("ABC".isupper())    # True
print("aBc".isalpha())    # True
print("123".isnumeric())  # True
print("abc123".isalnum()) # True

# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
