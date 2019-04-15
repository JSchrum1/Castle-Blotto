import Castle
import player as playerClass

# By Joe Schrum
# Email JoeSchrum1@gmail.com with questions or comments

#Print scores from each game for a particular player
#Input: List, int (gamesList, number of chosen player)
def head2heads(gamesList, pNum):
    playerCastles=gamesList.pop(pNum)
    Scores=[]
    for entry in gamesList:
        p1Score, p2Score=Castle.findScores(playerCastles, entry)
        Scores.append([p1Score, p2Score, entry[10]])
    return Scores, playerCastles[10]

#Finds and returns stats for a certain 1v1 match given the 2 player lists
def oneVSone(p1, p2):
    r=[] #win, loss, tie, or match never occurs for player 1 for each castle
    tLeft=[0,0,0,0,0,0,0,0,0,0,0,0] #Troops player 1 won by
    tLostby=[0,0,0,0,0,0,0,0,0,0,0,0] #Troops player 1 lost by
    tUnused=[0,0,0,0,0,0,0,0,0,0,0,0] #Troops unused for player 1 (if castle battle never occurs)
    troops=[0,0,0,0,0,0,0,0,0,0] # Number of troops player 1 has on each castle
    score=[[0,0]] #Current score [player 1, player 2] after each castle
    first=True #Used to ensure the score function doesn't try to access an invalid list element on the first iteration
    winner=False #True if the castles no longer matter because a winner has already been chosen
    cWon=0 #Number of castles won
    cLost=0 #Number of castles lost
    cUnused=0 #Number of castles where the battle doesn't occur
    for castle in range(10):
        troops[castle]=p1[castle]
        if not winner:
            if(p1[castle]>p2[castle]):
                r.append("Win")
                tLeft[castle]=p1[castle]-p2[castle]
                cWon+=1
                if(first):
                    score[0][0]=1
                    first=False
                else:
                    score.append([(score[castle-1][0]+(castle+1)),score[castle-1][1]])
            elif(p1[castle]<p2[castle]):
                r.append("Loss")
                tLostby[castle]=p2[castle]-p1[castle]
                cLost+=1
                if(first):
                    score[0][1]=1
                    first=False
                else:
                    score.append([(score[castle-1][0]),(score[castle-1][1]+(castle+1))])
            else:
                r.append("Tie")
                if not(first):
                    score.append([score[castle-1][0],score[castle-1][1]])
                else:
                    first=False
            if(score[castle][0]>=20 or score[castle][1]>=20):
                winner=True
        else:
            cUnused+=1
            tUnused[castle]=p1[castle]
            score.append([score[castle-1][0],score[castle-1][1]])
    for x in range(10):
        tLostby[10]+=tLostby[x]
        tLeft[10]+=tLeft[x]
        tUnused[10]+=tUnused[x]
        r.append("N/A")
    if(score[9][0]>score[9][1]):
        final="Win"
    elif(score[9][0]<score[9][1]):
        final="Loss"
    else:
        final="Tie"
    try:
        tLostby[11]=(round((tLostby[10]/cLost),1))
    except:
        tLostby[11]=0
    try:
        tUnused[11]=(round((tUnused[10]/cUnused),1))
    except:
        tUnused[11]=0
    try:
        tLeft[11]=(round((tLeft[10]/cWon),1))
    except:
        tLeft[11]=0
    return r, tLeft, tLostby, tUnused, score, final

#Print 1v1 match results given results from oneVSone function
def printoneVSone(p1, p2):
    #r= List containing result of each match
    #tLeft= List containing Troops player1 won by at each castle won, tLeft[10] is total of 0-9
    #tLostby= List of how many troops you lost by at each tower lost, tLostby[10] is total of 0-9
    #tUnused List containing number of troops at each castle where a battle was not fought because the match already ended, tUnused[10] is total of 0-9
    #score=List containing the score after each castle. Each element is a List of 2 integers, with the first being player 1's cumulative score and the second being player 2's cumulative score
    r, tLeft, tLostby, tUnused, score, final=oneVSone(p1, p2)
    print("{:34}{:>20} vs {:<}, Match Results: {}".format("",p1[10],p2[10],final))
    print("{:>20}  {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(" ","Castle 1", "Castle 2", "Castle 3", "Castle 4", "Castle 5", "Castle 6", "Castle 7", "Castle 8", "Castle 9", "Castle 10"))
    print("{:>20}: C1: {:<3}   C2: {:<3}   C3: {:<3}   C4: {:<3}   C5: {:<3}   C6: {:<3}   C7: {:<3}   C8: {:<3}   C9: {:<3}   C10: {:<3}".format(p1[10],p1[0],p1[1],p1[2],p1[3],p1[4],p1[5],p1[6],p1[7],p1[8],p1[9]))
    print("{:>20}: C1: {:<3}   C2: {:<3}   C3: {:<3}   C4: {:<3}   C5: {:<3}   C6: {:<3}   C7: {:<3}   C8: {:<3}   C9: {:<3}   C10: {:<3}".format(p2[10],p2[0],p2[1],p2[2],p2[3],p2[4],p2[5],p2[6],p2[7],p2[8],p2[9]))
    print("{:>20}: {:<7}   {:<7}   {:<7}   {:<7}   {:<7}   {:<7}   {:<7}   {:<7}   {:<7}   {:<7}".format("Results", r[0], r[1], r[2], r[3],r[4],r[5],r[6],r[7],r[8],r[9])) #Win, Loss, or Tie, UNPLAYED
    print("{:>20}: {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  {:<2} to {:<2}  ".format("Score", score[0][0],score[0][1],score[1][0],score[1][1],score[2][0],score[2][1],score[3][0],score[3][1],score[4][0],score[4][1],score[5][0],score[5][1],score[6][0],score[6][1],score[7][0],score[7][1],score[8][0],score[8][1],score[9][0],score[9][1],))#comulative score
    print("{:>20}: C1: {:<3}   C2: {:<3}   C3: {:<3}   C4: {:<3}   C5: {:<3}   C6: {:<3}   C7: {:<3}   C8: {:<3}   C9: {:<3}   C10: {:<3}   Total: {:<3}   Average: {:<3}".format("Troops Won by", tLeft[0],tLeft[1],tLeft[2],tLeft[3],tLeft[4],tLeft[5],tLeft[6],tLeft[7],tLeft[8],tLeft[9],tLeft[10], tLeft[11]))#troops left
    print("{:>20}: C1: {:<3}   C2: {:<3}   C3: {:<3}   C4: {:<3}   C5: {:<3}   C6: {:<3}   C7: {:<3}   C8: {:<3}   C9: {:<3}   C10: {:<3}   Total: {:<3}   Average: {:<3}".format("Troops Lost by", tLostby[0],tLostby[1],tLostby[2],tLostby[3],tLostby[4],tLostby[5],tLostby[6],tLostby[7],tLostby[8],tLostby[9],tLostby[10], tLostby[11]))#troops lost by
    print("{:>20}: C1: {:<3}   C2: {:<3}   C3: {:<3}   C4: {:<3}   C5: {:<3}   C6: {:<3}   C7: {:<3}   C8: {:<3}   C9: {:<3}   C10: {:<3}   Total: {:<3}   Average: {:<3}\n".format("Troops Unused", tUnused[0],tUnused[1],tUnused[2],tUnused[3],tUnused[4],tUnused[5],tUnused[6],tUnused[7],tUnused[8],tUnused[9],tUnused[10], tUnused[11]))#troops unused
    return r, tLeft, tLostby, tUnused, score, final

#Print average 1v1 stats for a certain player given the list of players and their playerID
def printAVG1v1only(gList, p1ID):
    allInfo=[]
    gamesList=gList.copy()
    pNum=playerClass.findpNum(gamesList, p1ID)
    p1=gamesList.pop(pNum)
    for player in gamesList:
        r, tLeft, tLostby, tUnused, score, final=oneVSone(p1, player)
        allInfo.append([r, tLeft, tLostby, tUnused, score, final])
    name=p1[10]
    troops=p1[0:10]
    printavg1v1(allInfo, name, troops)

#Prints all player 1v1 info for a certain player given the player list and their player ID
def printAllplayer1v1(gList, p1ID):
    allInfo=[]
    gamesList=gList.copy()
    pNum=playerClass.findpNum(gamesList, p1ID)
    p1=gamesList.pop(pNum)
    printH2H(gList, p1[12])
    print("\n{:42}{}'s castle by castle results for all matches\n".format("",p1[10]))
    for player in gamesList:
        r, tLeft, tLostby, tUnused, score, final=printoneVSone(p1, player)
        allInfo.append([r, tLeft, tLostby, tUnused, score, final])
    name=p1[10]
    troops=p1[0:10]
    printavg1v1(allInfo, name, troops)

#Prints all 1v1 info for all players given the player list
def printAll1v1(gamesList):
    for player in gamesList:
        printAllplayer1v1(gamesList, player[12])

#Prints all average 1v1 info given the player list
def printAllAVG1v1(gamesList):
    for player in gamesList:
        printAVG1v1only(gamesList, player[12])

#Prints average 1v1 info for a certain player given their info, name, and troop distribution
def printavg1v1(allInfo, name, troops):
    CWP, CLP, CTP, CUP, CAVGW, CAVGL, WOC, LOC, AVGCW, AVGCL, AVGWM, AVGLM, AVGOU, PO20=avg1v1(allInfo)
    print("\n{:>70}{:<}\n".format("Statistics for ",name))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castle Number","Castle 1","Castle 2", "Castle 3", "Castle 4", "Castle 5", "Castle 6", "Castle 7", "Castle 8", "Castle 9", "Castle 10"))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Troop Count",troops[0],troops[1],troops[2],troops[3],troops[4],troops[5],troops[6],troops[7],troops[8],troops[9]))#troop count
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castle Win %",CWP[0],CWP[1],CWP[2],CWP[3],CWP[4],CWP[5],CWP[6],CWP[7],CWP[8],CWP[9]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castles Average Win By",CAVGW[0],CAVGW[1],CAVGW[2],CAVGW[3],CAVGW[4],CAVGW[5],CAVGW[6],CAVGW[7],CAVGW[8],CAVGW[9]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castles Loss %",CLP[0],CLP[1],CLP[2],CLP[3],CLP[4],CLP[5],CLP[6],CLP[7],CLP[8],CLP[9]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castles Average Loss by",CAVGL[0], CAVGL[1], CAVGL[2], CAVGL[3], CAVGL[4], CAVGL[5], CAVGL[6], CAVGL[7], CAVGL[8], CAVGL[9]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castles Tie %",CTP[0],CTP[1],CTP[2],CTP[3],CTP[4],CTP[5],CTP[6],CTP[7],CTP[8],CTP[9]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Castles Unused %",CUP[0],CUP[1],CUP[2],CUP[3],CUP[4],CUP[5],CUP[6],CUP[7],CUP[8],CUP[9]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Wins on Castle","N/A","N/A","N/A","N/A","N/A",WOC[0],WOC[1],WOC[2],WOC[3],WOC[4]))
    print("{:>30}: {:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Losses on Castle","N/A","N/A","N/A","N/A","N/A",LOC[0],LOC[1],LOC[2],LOC[3],LOC[4]))
    print("{:>30}: {}".format("Average Castle Victory",AVGCW))
    print("{:>30}: {}".format("Average Castle Loss",AVGCL))
    print("{:>30}: {}".format("Average Win Margin",AVGWM))
    print("{:>30}: {}".format("Average Loss Margin",AVGLM))
    print("{:>30}: {}".format("Average Over/Under",AVGOU))
    print("{:>30}  {:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}".format("","0","1","2","3","4","5","6","7","8","9"))
    print("{:>30}: {:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}{:^4}".format("Games won by amount over 20",PO20[0],PO20[1],PO20[2],PO20[3],PO20[4],PO20[5],PO20[6],PO20[7],PO20[8],PO20[9]))

#  info[x][0]=r  info[x][1]=tLeft  info[x][2]=tLostby  info[x][3]=tUnused  info[x][4]=score   info[x][5]=final
# Finds average 1v1 info for a player given their match 1v1 info
def avg1v1(info):
    cWinPercent=[] #percent of times player won each castle
    cLossPct=[] #percent of time player lost each castle
    cTiePct=[] #percent of time player tied each castle
    cUnusedPct=[] #percent of time castle was not played for a player
    cAvgWinBy=[] #Average number of troops player won a castle by
    cAvgLoseBy=[] #average number of troops player lost a castle by
    winsOnCastle=[0,0,0,0,0] #wins from each castle 6-10
    LossOnCastle=[0,0,0,0,0] #losses on each castle from 6-10
    avgCVictory=-1 #average castle number you win on
    avgCLoss=-1 #The average castle on which the player loses a match
    avgWinMargin=-1 #Average Amount you win by (in points)
    avgLossMargin=-1 #average amount you lose by (in points)
    avgOU=-1 #average amount of points over or under your opponent for your matches
    pointsOver20=[0,0,0,0,0,0,0,0,0,0] #starting at 0 points over 20, how many wins were by each margin over 20

    matchCount=len(info)
    CW=0
    CWC=0
    CL=0
    CLC=0
    TWM=0
    TLM=0
    OU=0
    for match in info:
        for castle in range(6,11):
            if(match[4][castle-1][0]>=20):
                winsOnCastle[castle-6]+=1
                CW+=castle
                CWC+=1
                difference=(match[4][castle-1][0]-match[4][castle-1][1])
                TWM+=difference
                OU+=difference
                wonBy=match[4][castle-1][0]-20
                pointsOver20[wonBy]+=1
                break
            elif(match[4][castle-1][1]>=20):
                CL+=castle
                CLC+=1
                LossOnCastle[castle-6]+=1
                difference=(match[4][castle-1][1]-match[4][castle-1][0])
                TLM+=difference
                OU-=difference
                break
    try:
        avgWinMargin=round((TWM/CWC),2)
        avgLossMargin=round((TLM/CLC),2)
        avgOU=round((OU/(CWC+CLC)),2)
        avgCVictory=round((CW/CWC),2)
        avgCLoss=round((CL/CLC),2)
    except:
        avgWinMargin=0
        avgLossMargin=0
        avgOU=0
        avgCVictory=0
        avgCLoss=0
    for castle in range(10):
        CW=0
        CT=0
        CL=0
        CU=0
        CWB=0
        CAL=0
        for match in range(matchCount):
            if(info[match][0][castle]=="Win"):
                CW+=1
                CWB+=info[match][1][castle]
            elif(info[match][0][castle]=="Tie"):
                CT+=1
            elif(info[match][0][castle]=="Loss"):
                CL+=1
                CAL+=info[match][2][castle]
            else:
                CU+=1
        try:
            cWinPercent.append(round((CW*100/matchCount),1))
            cLossPct.append(round((CL*100/matchCount),1))
            cTiePct.append(round((CT*100/matchCount),1))
            cUnusedPct.append(round((CU*100/matchCount),1))
        except:
            cWinPercent.append(0)
            cLossPct.append(0)
            cTiePct.append(0)
            cUnusedPct.append(0)
        try:
            cAvgWinBy.append(round((CWB/CW),1))
        except:
            cAvgWinBy.append(0)
        try:
            cAvgLoseBy.append(round((CAL/CL),1))
        except:
            cAvgLoseBy.append(0)
    return cWinPercent, cLossPct, cTiePct, cUnusedPct, cAvgWinBy,cAvgLoseBy,winsOnCastle,LossOnCastle,avgCVictory,avgCLoss,avgWinMargin,avgLossMargin,avgOU,pointsOver20

#print basic head to head info for a player given the list of players and their player ID
def printAllplayerh2h(gList, ID):
    gamesList=gList.copy()
    printH2H(gamesList, ID)
    p1=playerClass.findpNum(gamesList, ID)
    printAll1v1(gamesList)

#print basic head to head info for all players given the list of players
def printAllh2h(gamesList):
    for player in gamesList:
        printAllplayerh2h(gamesList, player[12])

#used to find basic info on 1v1 stats, which it returns to the function which called it
def printH2H(gList, ID):
    gamesList=gList.copy()
    pNum=playerClass.findpNum(gamesList, ID)
    scores, name=head2heads(gamesList, pNum)
    wins=0
    losses=0
    ties=0
    print("\n{:3}{} Head to Head Matches\n".format("",name))
    for match in scores:
        p1Score=match[0]
        p2Score=match[1]
        result=""
        if(p1Score>p2Score):
            wins+=1
            result="Win"
        elif(p2Score>p1Score):
            losses+=1
            result="Loss"
        else:
            ties+=1
            result="Tie"
        print("{:>4}  to  {:<4} {:<5} against {:<20}".format(p1Score, p2Score, result, match[2]))
    try:
        print("Wins: {:4}, Losses: {:4}, Ties: {:3}, Win %: {:6}".format(wins, losses, ties, round(((2*wins+ties)*100)/(2*(wins+losses+ties)), 1)))
    except:
        print("Wins: {:4}, Losses: {:4}, Ties: {:3}, Win %: {:6}".format(wins, losses, ties, 0))
