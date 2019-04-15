# Joseph Schrum
# Joeschrum1@gmail.com

#Given a list of lists containing player info, prints results of the tournament
def printRecord(List):
    records=CheckGames(List)
    sortedRecords=sortRecords(records)
    for x in range(len(sortedRecords)):
        printInfo(sortedRecords[x])

#prints results for a specific player
def printInfo(playerStats):
    print("{:20} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7}".format(playerStats[0], playerStats[7], playerStats[5], playerStats[1], playerStats[2], playerStats[3], playerStats[4], playerStats[6]))

#sorts tournament results given a list of the results and assigns ranks and percentiles
#Returns a new list, not an in place sort
def sortRecords(records):
    r=records
    sortedRecords=[]
    sortedRecords.append(r.pop(0))
    rank=1
    while(len(r)>=1):
        greatest=r[0][4]
        greatestNum=0
        x=1
        while(x<len(r)):
            if(r[x][4]>greatest):
                greatest=r[x][4]
                greatestNum=x
            x+=1
        sortedRecords.append(r.pop(greatestNum))
        lastElement=len(sortedRecords)-1
        sortedRecords[lastElement][5]=rank
        try:
            percentile=round((1-((rank-1)/(len(records)-1+len(sortedRecords)-1)))*100, 1)
        except:
            percentile=0
        sortedRecords[lastElement][6]=percentile
        if(lastElement>0):
            if(sortedRecords[lastElement][4]==sortedRecords[lastElement-1][4]):
                sortedRecords[lastElement][5]=sortedRecords[lastElement-1][5]
                sortedRecords[lastElement][6]=sortedRecords[lastElement-1][6]
        rank+=1
    return sortedRecords

#Finds score of a head to head match given player list
def findScores(player1Distro, player2Distro):
    player1Score=0
    player2Score=0
    for castle in range(1, 11):
        if(player1Distro[castle-1]>player2Distro[castle-1]):
            player1Score+=castle
        elif(player2Distro[castle-1]>player1Distro[castle-1]):
            player2Score+=castle
        if(player1Score >= 20 or player2Score >= 20):
            return player1Score, player2Score
    return player1Score, player2Score

#Finds winner by calling findScores given 2 players' lists
def findWinner(p1Distro, p2Distro):
    p1Score, p2Score=findScores(p1Distro, p2Distro)
    if(p1Score> p2Score):
        return 1
    if(p2Score > p1Score):
        return 2
    return -1

#Finds wins losses and ties for a certain player given their list index number and the list of players
def findRecord(gameNumber, Entries):
    wins=0
    losses=0
    ties=0
    Troops=0
    for castle in range(10):
        Troops+=Entries[gameNumber][castle]
    if(Troops>100):
        return 0, 0, 0
    for entry in range(len(Entries)):
        if not (gameNumber == entry):
            x=findWinner(Entries[gameNumber], Entries[entry])
            if(x==1):
                wins+=1
            if(x==2):
                losses+=1
            if(x==-1):
                ties+=1
    return wins, losses, ties

#Finds all players' records given the list of players
def CheckGames(gamesList):
    Records= [["Contestant", "Wins", "Losses", "Ties", "Win %", "Rank", "Percentile", "ID"]]
    for entry in range(len(gamesList)):
        W, L, T = findRecord(entry, gamesList)
        try:
            temp= [gamesList[entry][10], W, L, T, round((2*W+T)*100/(2*(W+L+T)), 1), -1, -1, gamesList[entry][12]]
        except:
            temp= [gamesList[entry][10], 0, 0, 0, 0, 0, 0, gamesList[entry][12]]
        Records.append(temp)
    return Records
