import Castle
import Groups
import head2head
 #  By Joe Schrum
 #  Email Joeschrum1@gmail.com for questions or comments

def addPlayer(playerList, infoReset=["NULL",0,0,0,0,0,0,0,0,0,0,[]]):
    info=infoReset.copy()
    if (info[0]=="NULL"):
        info[0]=input("Enter player name: ")
        for castle in range(1,11):
            try:
                info[castle]=int(input("Enter troops in castle {}: ".format(castle)))
                if(info[castle]<0 or info[castle]>100):
                    raise Exception
            except:
                print("Not a valid integer, Castle {} has been given 0 troops.".format(castle))
                info[castle]=0
        group=input('Please enter group ID of any groups this player belongs to one at a time, or "Quit" to exit: ').lower()
        while not(group=="quit" or group =="q" or group==""):
            try:
                info[11].append(int(group))
            except:
                print('Please enter a valid integer, or "Quit" to exit. ')
            group=input('Please enter group ID of any groups this player belongs to, or "Quit" to exit: ').lower()
    if not(checkTroopCount(info[1:11])):
        print("Failed to add player")
        return
    playerObject=[]
    playerObject.append(player(info[0], info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10],info[11]))
    playerList.extend(makePlayerArray(playerObject))

def deletePlayer(playerList, idNum=-1):
    if(idNum==-1):
        try:
            idNum=int(input("Please enter the ID of the player you would like to delete: "))
        except:
            print("Not a valid integer.")
            return
    index=findpNum(playerList, idNum)
    del playerList[index]

def findpNum(gamesList, ID):
    x=0
    for player in gamesList:
        if (player[12]==ID):
            return x
        x+=1
    print("Player ID Invalid")
    exit(0)

def printPlayer(playerList, idNum):
    index=findpNum(playerList, idNum)
    player=playerList[index]
    print("{:<20} ID: {:<5} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^10}".format(player[10], player[12],player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8],player[9]))

def editName(playerList, idNum, name="NULL"):
    index=findpNum(playerList, idNum)
    if(name=="NULL"):
        printPlayer(playerList, idNum)
        playerList[index][10]=input("Enter player's new name: ")
    else:
        playerList[index][10]=name
    print("Name change successful")
    printPlayer(playerList, idNum)

def editCastles(playerList, idNum, troopsReset=[0,0,0,0,0,0,0,0,0,0]):
    troops=troopsReset.copy()
    index=findpNum(playerList, idNum)
    if(troops==[0,0,0,0,0,0,0,0,0,0]):
        printPlayer(playerList, idNum)
        for x in range(0,10):
            try:
                troops[x]=int(input("Enter troops for castle {}:".format(x+1)))
                if(troops[x]<0 or troops[x]>100):
                    raise Exception
            except:
                print("Input not a valid integer. Castle {} has been assigned 0 troops.".format(x+1))
        valid=checkTroopCount(troops)
        if not(valid):
            print("Troop change failed.")
        else:
            for castle in range(0,10):
                try:
                    playerList[index][castle]=int(troops[castle])
                except:
                    print("Found non-valid value. Castle {} assigned 0 troops.".format(castle+1))
            print("Troop change successful.")
            printPlayer(playerList, idNum)

def addGroup(playerList, idNum, groupList, groupID=-1):
    index=findpNum(playerList, idNum)
    if(groupID==-1):
        groupID=input("Please enter the group ID of the group you would like to add this player to: ")
    try:
        groupID=int(groupID)
    except:
        print("Not a valid integer. Group add failed.")
        return
    if groupID in playerList[index][11]:
        print("Player already in group {}".format(groupID))
    else:
        playerList[index][11].append(groupID)
        print("Player added successfully.")
        Groups.printGroup(playerList, groupID, groupList)

def removeGroup(playerList, idNum, groupID=-1):
    index=findpNum(playerList, idNum)
    if(groupID==-1):
        groupID=input("Please enter the group ID of the group you would like to remove this player from: ")
    try:
        groupID=int(groupID)
    except:
        print("Not a valid integer. Group removal failed")
        return
    if not groupID in playerList[index][11]:
        print("This player is not in this group.")
    else:
        for x in range(0, len(playerList[index][11])):
            if(playerList[index][11][x]==groupID):
                del playerList[index][11][x]
                print("Player Successfully removed from group {}.".format(groupID))
                return

def checkTroopCount(troopList):
    totalTroops=0
    for castle in range(0,10):
        totalTroops+=troopList[castle]
    if(totalTroops>100):
        print("Too many troops. Total troop count is {}".format(totalTroops))
        return False
    return True

def printPlayerList(playerList):
    print("{:^20} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9}".format("Name","ID", "Castle 1","Castle 2","Castle 3","Castle 4","Castle 5", "Castle 6", "Castle 7", "Castle 8", "Castle 9", "Castle 10"))
    averages=[0,0,0,0,0,0,0,0,0,0]
    for player in playerList:
        print("{:<20} ID: {:<5} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^10}".format(player[10], player[12],player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8],player[9]))
        for castle in range(0,10):
            averages[castle]+=player[castle]
    playerCount=len(playerList)
    for i in range(0,10):
        try:
            averages[i]=round((averages[i]/playerCount),1)
        except:
            averages[i]=0
    print("{:^20} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9}".format("","", "Castle 1","Castle 2","Castle 3","Castle 4","Castle 5", "Castle 6", "Castle 7", "Castle 8", "Castle 9", "Castle 10"))
    print("{:<20} {:<9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^9} {:^10}".format("Average","",averages[0],averages[1],averages[2],averages[3],averages[4],averages[5],averages[6],averages[7],averages[8],averages[9]))


#This turns the list of player objects into a list of lists to work with other functions
#10 castles, then p[10]=name, p[11]=groups, p[12]=ID
def makePlayerArray(List):
    players=[]
    for p in List:
        players.append([p.c1, p.c2, p.c3, p.c4, p.c5, p.c6, p.c7, p.c8, p.c9, p.c10, p.name, p.groups, p.ID])
    return players


class player:
    IDnum=101
    def __init__(self, name="Null", c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0, c9=0, c10=0, groups=[]):
        totalTroops=c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
        if(totalTroops>100):
            print("{} has too many troops! Failed to create player".format(name))
            return
        elif(totalTroops<100):
            print("\n{} only has {} troops!\n\n".format(name, totalTroops))
        self.name=name
        self.ID=self.IDnum
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.c4=c4
        self.c5=c5
        self.c6=c6
        self.c7=c7
        self.c8=c8
        self.c9=c9
        self.c10=c10
        self.groups=groups
        player.IDnum+=1
