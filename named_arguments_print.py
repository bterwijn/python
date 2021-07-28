
# help(print)

print('One')             # One\n
print('One', end='END')  # OneEND
print('One', end='')     # One

print('One', 'Two', 'Three', end='END')            # One Two ThreeEND
print('One', 'Two', 'Three', sep='__', end='END')  # One__Two__ThreeEND
