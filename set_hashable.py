
my_set = set()
my_set.add( 123 )
my_set.add( 'Hello World' )
my_set.add( (1, 2, 'Hi') )
print(my_set)  # {'Hello World', 123, (1, 2, 'Hi')}

# my_set.add( [100,200] )   # TypeError: unhashable type: 'list'
# my_set.add( {100,200} )   # TypeError: unhashable type: 'set'

my_set.add( tuple([100, 200]) )
print(my_set)  # {'Hello World', 123, (1, 2, 'Hi'), (100, 200)}
print( tuple([100, 200]) in my_set)  # True

my_set.add( str([100, 200]) )

my_set.add( frozenset({100, 200}) )