'''Maak een sneeuw-animatie. Representeer hiervoor met een tabel
(lijst van lijsten) een stuk luchtruim van 10 posities hoog en 20
breed gevuld met het '.' teken, een lege plek. Schrijf:
- een functie die het luchtruim aanmaakt
- een functie die het luchtruim print
- een functie die elk teken op de bovenste regel van het luchtruim met 
een kans van 0.05 vervangt door het '*' teken, een sneewvlok
- een functie die elke sneeuwvlok een positie naar beneden verplaatst 
als daar een '.' teken staat

Gebruik deze functies om een sneeuw-animatie te maken. 

hint:

  print(random.random() < 0.05) # print 'True' met een kans van 0.05, en anders 'False'

'''
import random
import time

def main():
    width = 20
    height = 10
    empty_cell = '.'
    snow_cell = '*'
    snow_chance = 0.05

main()
