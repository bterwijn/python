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
    pairs = [ (p1,p2)
              for p1 in participants
              for p2 in participants
              if len(p1)+len(p2)<=max_length and p1<p2]
    print(pairs) # [('Emily', 'Matthew'), ('Emily', 'Margaret'), ('Margaret', 'Matthew')]

main()
