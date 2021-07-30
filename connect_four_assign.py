''' Maak een 4-op-een-rij spel

Het spel heeft een bord van 6 hoog en 7 breed. Twee Spelers gooien
omstebeurt herhaaldelijk een steen in het bord. Een steen valt naar
beneden totdat het boven op de onderkant van het bord of op een andere 
steen komt te liggen. Het spel eindigt als het bord helemaal gevuld is 
of als een speler 4 of meer stenen op een rij heeft. Een rij kan 
hierbij vertikaal, horizontaal, of diagonaal zijn.

Vraag steeds aan de speler die aan de beurt is in welke kollom hij/zij
de steen wil gooien en herhaal de vraag als het gegeven antwoord niet
mogelijk is.

Het programma eindigd met een van deze regels:

  WINNER: Player1
  WINNER: Player2
  DRAW

'''

def main():
    width = 7
    height = 6
    empty_cell = '.'
    players = [('Player1', 'X'), ('Player2', 'O')]
    move_count = 0
    
def input_integer(question):
    """ Keeps asking the user a 'question' until the user enters an
        integer which is returned """
    while True:
        try:
            integer=int(input(question))
            break
        except ValueError:
            print('not and integer :(')
    return integer

main()
