''' Maak met een list comprehension een lijst van tuples met alle
mogelijke paren van 2 van de deelnemers waarbij de lengte van de beide
namen kleiner dan of gelijk aan 'max_length' moet zijn. Voorkom
dubbele paren waarbij (A,B) en (B,A) dubbele paren zijn.

hints: 
  print(len('Christopher')) # 11      lengte van de naam
  print('Emily'<'Matthew')  # True    'Emily' is alfabetisch kleiner dan 'Matthew'

'''

def main():
    participants = ['Christopher', 'Emily', 'Matthew', 'Margaret']
    max_length = 15
    pairs = [ # add your code here
             ]
    print(pairs) # [('Emily', 'Matthew'), ('Emily', 'Margaret'), ('Margaret', 'Matthew')]

main()
