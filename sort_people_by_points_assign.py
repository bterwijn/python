'''Sorteer personen op basis van hun corresponderende punten en geef de top-N met de meeste punten. '''

def main():
    people = ["Henk", "Jane", "Laura", "Bill", "Ana"]
    points = [46, 87, 59, 73, 61]
    top_3 = get_top_n(3, people, points)
    print(top_3)  # ['Jane', 'Bill', 'Ana']

def get_top_n(n, people, points):
    """ Returns the top 'n' 'people' with the most corresponding 'points' """
    pass # add your code here

main()
