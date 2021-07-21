''' Sorteer personen op basis van het hun punten en geef de top-N met de meeste punten. '''

def main():
    people = ["Henk", "Jane", "Laura", "Bill", "Ana"]
    points = [46, 87, 59, 73, 61]
    top_3 = get_top_n(3, people, points)
    print(top_3)  # ['Jane', 'Bill', 'Ana']
    top_3 = get_top_n_alternative(3, people, points)
    print(top_3)  # ['Jane', 'Bill', 'Ana']

def get_top_n(n, people, points):
    """ Returns the top 'n' 'people' with the most corresponding 'points' """
    combine = [ (person, points[index]) for index, person in enumerate(people)] 
    # [('Henk', 46), ('Jane', 87), ('Laura', 59), ('Bill', 73), ('Ana', 61)]
    combine.sort(key=lambda person_points: -person_points[1]) 
    # [('Jane', 87), ('Bill', 73), ('Ana', 61), ('Laura', 59), ('Henk', 46)]
    return [i[0] for i in combine[:n]]

def get_top_n_alternative(n, people, points):
    indices = list(range(len(people)))                   # [0, 1, 2, 3, 4]
    indices.sort(key=lambda i: points[i], reverse=True)  # [1, 3, 4, 2, 0]
    return [people[i] for i in indices[:n]]

main()