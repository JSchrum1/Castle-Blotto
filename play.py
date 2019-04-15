import player
import Castle
import head2head
import Groups

def main():
    playerList, groupList=initialize()
    sure="no"
    while not (sure=="y" or sure=="yes" or sure=="quit" or sure=="q"):
        userInput=input("Enter a command: ").lower()
        while(userInput != "quit" and userInput != "exit" and userInput !="q"):
            userInput=processCommand(userInput, playerList, groupList)
        sure=input("Are you sure you would like to exit? [y/n]:").lower()
    print("Thank you for playing!")

def printWelcome():
    print("Welcome to Castle Blotto!")
    print("This is a strategy based tournament style game.")
    print("Take your time before you answer and consider what you think your opponent will do.")
    print("Good luck!")

def printRules():
    print(
"""
Castle Blotto Rules:
1.) Each player gets 100 troops to distribute among 10 castles. 
2.) Each Castle is worth it's number of points (castle 1 is worth 1 point, castle 2 is worth 2 points, etc.)
3.) Castles are fought starting at castle 1 and go in order
4.) You get the points from the castle if you have more troops on that castle than your opponent does.
5.) If both people have the same number of troops on a castle, neither person gets any points.
6.) First person to 20 points wins each match. After someone gets to 20 points, the remaining castles don't count.
7.) Each player's entry will play every other player's entries.
8.) The person with the most head to head wins is the overall winner.""")

def printHelp():
    print(
"""
Help Message:
To add a player:                      Type "Add player"
To delete a player:                   Type "Delete player"
To show a list of all players:        Type "Show players"
To edit a player's info:              Type "Change player info"
To show results:                      Type "Show results"
To show group results:                Type "Group results" 
To see detailed match by match info:  Type "Print match info"
To create a group:                    Type "Create group"
To exit:                              Type "Quit"
To view the rules again:              Type "Rules"
To view this help message again:      Type "Help"
You may also use abbreviations for most commands.
"""
    )

def processCommand(userInput, playerList, groupList):
    if(userInput == "add player" or userInput=="ap"):
        player.addPlayer(playerList)
    elif(userInput == "change player info" or userInput=="cpi"):
        processChangePlayerInfo(playerList, groupList)
    elif(userInput == "show results" or userInput=="sr"):
        Castle.printRecord(playerList)
    elif(userInput == "print match info" or userInput=="pmi"):
        processPrintMatchInfo(playerList)
    elif(userInput == "show players" or userInput=="sp"):
        player.printPlayerList(playerList)
    elif(userInput == "delete player" or userInput=="dp"):
        player.deletePlayer(playerList)
    elif(userInput == "help" or userInput == "h" or userInput == "show help" or userInput== "sh"):
        printHelp()
    elif(userInput == "rules" or userInput == "r" or userInput=="show rules"):
        printRules()
    elif(userInput == "create group" or userInput =="cg"):
        Groups.createGroup(groupList)
    elif(userInput== "group results" or userInput=="gr"):
        showGroupResults(playerList, groupList)
    else:
        print("Invalid command.")
    return input("Enter a command: ").lower()

def showGroupResults(playerList, groupList):
    try:
        groupNum=int(input("Enter group number: "))
    except:
        print("Invalid group ID")
        return
    group=Groups.makeGroup(playerList, groupNum)
    try:
        print("Results within {} group:".format(groupList[groupNum-1]))
    except:
        print("Results within unnamed group {}:".format(groupNum))
    Castle.printRecord(group)
    details=input("Would you like to view detailed match by match info? [y/n]: ").lower()
    if(details=="yes" or details =="y"):
        head2head.printAll1v1(group)

def processPrintMatchInfo(playerList):
    userInput=input('Enter a playerID to see that player\'s stats or enter "All" to view all player stats: ').lower()
    if(userInput=="all" or userInput=="a"):
        head2head.printAll1v1(playerList)
        return
    try:
        ID=int(userInput)
    except:
        print("Invalid input.")
        return
    head2head.printAllplayer1v1(playerList, ID)

def processChangePlayerInfo(playerList, groupList):
    try:
        idNum=int(input("Please enter the ID number of the player you would like to edit: "))
    except:
        print("Input must be a valid integer")
        return
    type=input("Would you like to change a player's name, troops, or groups?: ").lower()
    if(type=="name" or type=="n"):
        player.editName(playerList, idNum)
    elif(type=="troops" or type =="t"):
        player.editCastles(playerList, idNum)
    elif(type=="groups" or type=="g"):
        editGroups(playerList, groupList, idNum)
    else:
        print("Invalid input.")

def editGroups(playerList,groupList,  idNum):
    addOrRemove=input("Would you like to add this player to a group or remove this player from  group?: ").lower()
    if(addOrRemove=="add" or addOrRemove=="a"):
        player.addGroup(playerList, groupList, idNum)
    elif(addOrRemove=="remove" or addOrRemove == "r"):
        player.removeGroup(playerList, idNum)
    else:
        print("Invalid input.")

def initialize():
    printWelcome()
    printRules()
    printHelp()
    playerList=[]
    groupList=[]
    return playerList, groupList

if __name__=="__main__":
    main()
