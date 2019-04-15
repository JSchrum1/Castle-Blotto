import player

# By Joe Schrum
# Email JoeSchrum1@gmail.com with questions or comments

#WARNING: The groups class may be buggy and has limited functionality as I did not actually use it so I did very little testing

#Returns a list containing only players belonging to that group given the list of all players and their groupID
def makeGroup(playerList, groupNum):
    group=[]
    for player in playerList:
        for groupID in player[11]:
            if(groupID==groupNum):
                group.append(player)
    return group

#Prints name and list of players in a certain group
def printGroup(playerList, groupNum, groupList):
    group=makeGroup(playerList, groupNum)
    try:
        print("Group Name: {}".format(groupList[groupNum-1]))
    except:
        print("Unnamed Group #{}".format(groupNum))
    player.printPlayerList(group)

#Creates a new group and allows you to name it
def createGroup(groupList, name="NULL"):
    if(name=="NULL"):
        name=input("Enter group name: ")
    if name in groupList:
        print("Group already exists.")
        return
    else:
        groupList.append(name)
