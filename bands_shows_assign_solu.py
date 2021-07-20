import copy

def main():
    bands = [ ['Ann','John'], ['Lisa','Paul','Judy'] ]
    shows = [] # schedule the bands for 4 shows
    shows.append( bands[0] )
    shows.append( bands[1] )
    shows.append( bands[0] )
    shows.append( bands[1] )
    print('shows:',shows)
    # [['Ann','John'], ['Lisa','Paul','Judy'], ['Ann','John'], ['Lisa','Paul','Judy']]

    # 'Amy' joins the band of Ann and John for all scheduled and future shows
    # add your code here
    bands[0].append('Amy')
    print('shows:',shows)
    # [['Ann','John','Amy'], ['Lisa','Paul','Judy'], ['Ann','John','Amy'], ['Lisa','Paul','Judy']]

    # 'Mark' will help Lisa,Paul,Judy as a guest performer in only the 4th show
    # add your code here
    index=4-1
    shows[index] = copy.copy(shows[index])
    shows[index].append('Mark')
    print('shows:',shows)
    # [['Ann','John','Amy'], ['Lisa','Paul','Judy'], ['Ann','John','Amy'], ['Lisa','Paul','Judy','Mark']]

    # 'Lisa' changes her stage name to 'LiZa' for all scheduled and future shows
    # add your code here
    bands[1][0] = 'LiZa'
    shows[index][0] = 'LiZa'
    print('shows:',shows)
    # [['Ann','John','Amy'], ['LiZa','Paul','Judy'], ['Ann','John','Amy'], ['LiZa','Paul','Judy','Mark']]
