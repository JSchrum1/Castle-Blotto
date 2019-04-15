import Castle
import Groups
import head2head
import player

def p(name="Null", c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0, c9=0, c10=0, groups=[]):
    return player.player(name,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,groups)

def main():
    pass

    playerList=makeList(starterPlayers())
    PrintRec(playerList)
    #printPlayers(playerList)
    #groupList=["Work", "College", "Sports"]
    printPlayer1v1(playerList, 119)
    #printAll1v1AVGs(playerList)

def printPlayers(playerList):
    player.printPlayerList(playerList)

def PrintRec(playerList):
    Castle.printRecord(playerList)

def makeList(List):
    return player.makePlayerArray(List)

def h2h(list, ID):
    head2head.printH2H(list, ID)

def printAVGplayer1v1(playerList, ID):
    head2head.printAVG1v1only(playerList, ID)

def printAll1v1AVGs(playerList):
    head2head.printAllAVG1v1(playerList)

def printAll1v1(playerList):
    head2head.printAll1v1(playerList)

def printPlayer1v1(playerList, ID):
    head2head.printAllplayer1v1(playerList, ID)

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
