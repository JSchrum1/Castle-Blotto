import player

def makeGroup(playerList, groupNum):
    group=[]
    for player in playerList:
        for groupID in player[11]:
            if(groupID==groupNum):
                group.append(player)
    return group

def printGroup(playerList, groupNum, groupList):
    group=makeGroup(playerList, groupNum)
    try:
        print("Group Name: {}".format(groupList[groupNum-1]))
    except:
        print("Unnamed Group #{}".format(groupNum))
    player.printPlayerList(group)

def createGroup(groupList, name="NULL"):
    if(name=="NULL"):
        name=input("Enter group name: ")
    if name in groupList:
        print("Group already exists.")
        return
    else:
        groupList.append(name)
