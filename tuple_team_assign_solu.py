'''Schrijf functie add_points() waarbij van een team het aantal
 verdiende punten en het aantal gespeelde wedstrijden kan worden
 bijgehouden.
'''

def main():
    team = ("FC Haarlem", 0, 0)  # a team starts with 0 played matches and 0 points
    team = add_points(team, 3)   # the team played a match and won 3 points
    team = add_points(team, 0)   # ...                             0
    team = add_points(team, 1)   # ...                             1

    print("team name:", team[0])       # FC Haarlem
    print("matches played:", team[1])  # 3
    print("total points:", team[2])    # 4

def add_points(team, points):
    """
    Returns a tuple indicating that 'team' earned 'points' in a new match.
    Arguments:
    team   -- the team (team_name, nr_matches, nr_point)
    points -- the number of points won in the new match
    """
    name, matches, total_points = team
    return (name, matches + 1, total_points + points)

main()
