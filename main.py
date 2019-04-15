import Castle
import Groups
import head2head
import player

# By Joe Schrum
# Email Joeschrum1@gmail.com with questions or comments

#calls function to create a new player
def p(name="Null", c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0, c9=0, c10=0, groups=[]):
    return player.player(name,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,groups)

# make a list of startplayers and print results and their 1v1 stats.
def main():
    playerList=makeList(starterPlayers())
    PrintRec(playerList)
    #printPlayers(playerList)
    #groupList=["Work", "College", "Sports"]
    printPlayer1v1(playerList, 119)
    #printAll1v1AVGs(playerList)

    #These functions are abbreviations to call functions in other classes easier
#print a list of players
def printPlayers(playerList):
    player.printPlayerList(playerList)

#Print results of the tournament
def PrintRec(playerList):
    Castle.printRecord(playerList)

#Turn the list of player onjects into a list of lists to be compatible with other code
def makeList(List):
    return player.makePlayerArray(List)

#Print the results of a certain player's head to head matches
def h2h(list, ID):
    head2head.printH2H(list, ID)

#Print the average stats of a certain player's head to head matches
def printAVGplayer1v1(playerList, ID):
    head2head.printAVG1v1only(playerList, ID)

#Print the average stats of all players' head to head matches
def printAll1v1AVGs(playerList):
    head2head.printAllAVG1v1(playerList)

#Print detailed info of every head to head match
def printAll1v1(playerList):
    head2head.printAll1v1(playerList)

#Print detailed info of all of one player's head to head matches
def printPlayer1v1(playerList, ID):
    head2head.printAllplayer1v1(playerList, ID)

#Initialize a list of players.
#I have kept my tournament's players here for an example of how it should be formatted
def starterPlayers():
    PL=[]
    # Name,                Castle #: 1   2   3   4   5   6   7   8   9  10,  groups
    PL.append(p("Joey Schrum",       2,  2,  2,  2, 21,  2, 33, 33,  2,  1,  [1,2,3]))
    PL.append(p("Adam",      0,  0,  2,  5, 10, 10, 15, 18, 20, 20,  [2]))
    PL.append(p("Aaron",      0,  0,  0,  0,  0, 20, 20, 20, 20, 20,  [1]))
    PL.append(p("Carson",     0,  0,  0,  0,  0, 34, 33, 33,  0,  0,  [2]))
    PL.append(p("Tommy",      5,  0,  0, 15, 20, 20, 20, 20,  0,  0,  [1,3]))
    PL.append(p("Anna",           0,  0,  0,  0, 22,  0, 39, 39,  0,  0)   )
    PL.append(p("Jake",       0,  0,  0,  0, 24, 26, 10,  0, 40,  0,  [2]))
    PL.append(p("Dylan",  3,  5,  8, 10, 13,  1, 26, 30,  2,  2)   )
    PL.append(p("Tyler",     15, 5, 15,  5, 15,  5, 15,  5, 15,  5,  [1]))
    PL.append(p("Mason",    1,  1,  1,  1,  1, 24, 34, 36,  1,  0,  [2]))
    PL.append(p("Katie",      10, 3, 36,  1,  1,  1,  0, 46,  1,  1,  [1]))
    PL.append(p("Nick",      0,  0,  0, 25, 25, 25, 25,  0,  0,  0,  [3]))
    PL.append(p("Dom",        0,  0,  0,  0,  0, 34, 33, 33,  0,  0,  [1]))
    PL.append(p("Reed",       3,  3,  4,  0,  0, 30, 30, 30,  0,  0,  [3]))
    PL.append(p("Alex",         0,  0, 10,  0,  0, 25, 25, 40,  0,  0,  [3]))
    PL.append(p("Alec",       1,  1,  1,  0, 31,  0, 31, 31,  0,  4))
    PL.append(p("Dan",       2,  2,  4,  6, 23, 21, 21, 21,  0,  0,  [1]))
    PL.append(p("Jarred",   15, 15, 15, 15, 15, 15, 10,  0,  0,  0,  [2]))
    PL.append(p("Jasmine",  0,  0, 15, 15, 10, 20, 11, 11, 17,  1))
    return PL

if __name__=="__main__":
    main()
