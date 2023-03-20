##############################  LU TABLE TENNIS ADMINISTRATION  ###############################
### Name:   Haochen Zhu
### Student ID: 1153918
################################################################################################## 

import lutt_admin_data       #lutt_admin_data.py contains the data lists and must be in the same folder as this file
import datetime

# The list variables
colTeams = lutt_admin_data.colTeams
dbTeams = lutt_admin_data.dbTeams

# These dictionaries define the columns for display for the different functions.

colPlayers = {'Team_Name':str,'Player_Name':str}

colDraw = {'First_Team': str, 'First_Score':int,'Second_Team': str, 'Second_Score':int}



def columnOutput(dbData,cols,formatStr):
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.
# For each column "{: <10}" determines the width of the column, padded with spaces (10 spaces in this example)
#   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
#   The following example is for 3 columns of output: left-aligned, 5 characters wide; centred, 10 characters; right-aligned 15 characters:
#       formatStr = "{: <5}  {: ^10}  {: >15}"
# Make sure the column is wider than the heading text and the widest entry in that column, otherwise the columns won't align correctly.
# You can also pad with something other than a space and put characters between the columns, 
# e.g. this pads with full stops '.' and separates the columns with the pipe character | :
#       formatStr = "{:.<5} | {:.^10} | {:.>15}"
    print(formatStr.format(*cols))
    for row in dbData:
        rowList=list(row)
        for index,item in enumerate(rowList):
            if item==None:      # Removes any None values from the rowList, which would cause the print(*rowList) to fail
                rowList[index]=""       # Replaces them with an empty string
            elif type(item)==datetime.date:    # If item is a date, convert to a string to avoid formatting issues
                rowList[index]=str(item)
        print(formatStr.format(*rowList))   


def listDraw():
    # Print out a copy of the draw. If listDraw() is operated before createDraw(), user will be notified.
    if drawCreatedOnce == False or drawList == []:
        print("\n*********************\n**  C A U T I O N  **\n*********************\nYou need to CREAT THE DRAW before listing the draw when\n      - Running the program at the first time\nOR    - Added new teams.\n")
        input('[Press Enter to Acknowledge]')

    print("\n=== DRAW LIST ===\n")
    colNames = {'TEAM 1': str, 'SCORE T1': int or bool,'TEAM 2': str, 'SCORE T2': int or bool}
    columnOutput(drawList,colNames,"|{0: ^20}|{1: ^10}| VS |{3: ^10}|{2: ^20}|")
    input("\nPress Enter to continue.")     # End function with this line

def listTeams():
    # Print a list of the teams
    displayList = []
    for team in dbTeams.keys():
        displayList.append((team,f'{dbTeams[team][0][0]} {dbTeams[team][0][1]}',f'{dbTeams[team][1][0]} {dbTeams[team][1][1]}'))
    print("\nALL TEAMS\n")
    columnOutput(displayList,colTeams,"|{: ^20} |{: ^20}|{: ^20}|") #example of how to call columnOutput function
    
    
    input("\nPress Enter to continue.")     # End function with this line
    

def listMembersSurnameAlpha():
    print('================')
    # print team member details in alphabetical order by last name then first name 
    # Create a playerlist and put tuple names in
    playerList = []
    for team in dbTeams.keys():
        playerList.append(dbTeams[team][0])
        playerList.append(dbTeams[team][1])
    print("\nALL PLAYERS (Sorted by surname and then firstname)\n")
    # Use lambda and sorted() to sort the names in the list by last name then first name
    sortFunc = lambda nameInTuple: (nameInTuple[1],nameInTuple[0])
    sortedPlayers = sorted(playerList,key=sortFunc)
    # Print it out by using columnOutput()
    colNames = {'FIRSTNAME': str, 'SURNAME': str}
    columnOutput(sortedPlayers,colNames,"|{: ^15}|{: ^15}|")
    input("\nPress Enter to continue.")     # End function with this line

def listMembersFirstnameAlpha():
    print('================')
    # print team member details in alphabetical order by first name then last name 
    # Create a playerlist and put tuple names in
    playerList = []
    for team in dbTeams.keys():
        playerList.append(dbTeams[team][0])
        playerList.append(dbTeams[team][1])
    print("\nALL PLAYERS (Sorted by firstname and then surname)\n")
    # Use lambda and sorted() to sort the names in the list by first name then last name
    sortFunc = lambda row: (row[0],row[1])
    sortedPlayers = sorted(playerList,key=sortFunc)
    # Print it out by using columnOutput()
    colNames = {'FIRSTNAME': str, 'SURNAME': str}
    columnOutput(sortedPlayers,colNames,"|{: ^15}|{: ^15}|")
    input("\nPress Enter to continue.")     # End function with this line

def addTeam():
    # add a team. Check a Player does not already exist.
    # Generate the team name and check that it does not already exist
    # Team Name is First Surname and Second Surname joined together each with an initial capital letter
    # =================
    # Function of checking if the player has already been registered in the other team
    def nameCheck(newNameTuple):
        playerList = []
        for team in dbTeams.keys():
            playerList.append(dbTeams[team][0])
            playerList.append(dbTeams[team][1])
        
        for names in playerList:
            if newNameTuple == names:
                return True
        return False
    
    player1Input = False
    player2Input = False
    # Registering the first new player
    while player1Input == False:
        print('================')
        newFirstname1 = str(input('Please type the firstname of player 1: ')).casefold().capitalize()
        newSurname1 = str(input('Please type the Surname of player 1: ')).casefold().capitalize()
        newName1Tuple = tuple((newFirstname1,newSurname1))
        #
        if newFirstname1.isnumeric() == True or newSurname1.isnumeric() == True:
            nameCheckFail = str(input("*********************\n**  C A U T I O N  **\n*********************\nThe player's name must contain alphabet letters. \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select: "))
            if nameCheckFail.upper() == 'Q':
                return print('Return menu. No new team added.')
        
        else:
        # If the player has been registered, the admin can either input a new name or leave the addTeam function
            while True:   
                if nameCheck(newName1Tuple) == True:
                    nameCheckFail = str(input('*********************\n**  C A U T I O N  **\n*********************\nThe player has been registered into another team! \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select: '))
                    if nameCheckFail.upper() == 'Q':
                        return print('Return menu. No new team added.')
                    break
                        
                else:
                    print('Player 1 name check PASSED.\n')
                    player1Input = True
                    break

    while player2Input == False:
        print('================')
        newFirstname2 = str(input('Please type the firstname of player 2: ')).casefold().capitalize()
        newSurname2 = str(input('Please type the Surname of player 2: ')).casefold().capitalize()
        newName2Tuple = tuple((newFirstname2,newSurname2))
        if newFirstname2.isnumeric() == True or newSurname2.isnumeric() == True:
            nameCheckFail = str(input("*********************\n**  C A U T I O N  **\n*********************\nThe player's name must contain alphabet letters. \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select: "))
            if nameCheckFail.upper() == 'Q':
                return print('Return menu. No new team added.')
        
        else:

        # If the player has been registered in other teams or in the player 1, the admin can either input a new name or leave the addTeam function
            while True:    
                if nameCheck(newName2Tuple) == True:
                    nameCheckFail = str(input('*********************\n**  C A U T I O N  **\n*********************\nThe player has been registered into another team! \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select: '))
                    if nameCheckFail.upper() == 'Q':
                        return print('Return menu. No new team added.')
                    break
                elif newName1Tuple == newName2Tuple:
                    nameCheckFail = str(input('*********************\n**  C A U T I O N  **\n*********************\nThe player name has been input as player 1! \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select: '))
                    if nameCheckFail.upper() == 'Q':
                        return print('Return menu. No new team added.')
                    break
                else:
                    print('Player 2 name check PASSED.\n')
                    player2Input = True
                    break
    
    # Check if teamName is unique. If not, another backup name consisting of reversed-ordered surname will be checked. 
    # If also not unique, user will be asked to create a new name.
    # The new name will also be checked.
    newTeamName = newSurname1 + newSurname2
    newTeamName2 = newSurname2 + newSurname1
    while True:
        for key in dbTeams.keys():
            if newTeamName.upper() == key.upper():
                for key in dbTeams.keys():
                    if newTeamName2 == None:
                        teamNameCheckResult = True
                        break
                    if newTeamName2.upper() == key.upper():
                        teamNameCheckResult = True
                        print("Sorry, the auto-generated team name '{}' and '{}' has been registered in the database.".format(newTeamName,newTeamName2))
                        break
                
                if teamNameCheckResult == True:
                    break
                newTeamName = newTeamName2
                teamNameCheckResult = False

            else:
                teamNameCheckResult = False
        
        if teamNameCheckResult == False:
            if newTeamName2 == newTeamName:
                print("********\nthe auto-generated team name '{}{}' has been registered by another team.\nThus, the new team's name has been changed to '{}'\n********\n".format(newSurname1,newSurname2,newTeamName))
            print('================')
            print('Team name check PASSED.\n')
            break
        elif teamNameCheckResult == True:
            newTeamName = str(input("Please create a different team name: "))
            newTeamName2 = None
    
    
    # Add new team to the dictionary
    dbTeams[newTeamName] = [newName1Tuple,newName2Tuple]
    global drawCreatedOnce
    drawCreatedOnce = False

    print(f"Congrats! The team has been registered succesfully.\nTeam: {newTeamName}\nPlayer1: {newFirstname1} {newSurname1}\nPlayer2: {newFirstname2} {newSurname2}")
    print('================')
    input('Press Enter to return to menu.')
    return



teamList = []
drawList = []
drawCreatedOnce = False
drawCreatedFirst = False
def createDraw():
    global teamList
    teamList = []
    global drawList
    global drawCreatedFirst
    global drawCreatedOnce
    # Each team should play each other team, but only once.
    # If the draw has been created once, and new teams are added after that, 
    # only new draws will be appended into the list in order to keep the match results of previous created draws.
    teamList = list(dbTeams.keys())
    for i in range(0, len(teamList)):
        for j in range(i, len(teamList)):
            if i != j:
                if drawCreatedFirst == False:
                    drawList.append(list([teamList[j],None,teamList[i],None]))
                else:
                    for draw in drawList:
                        possibility1 = draw[0] == teamList[j] and draw[2] == teamList[i]
                        possibility2 = draw[2] == teamList[j] and draw[0] == teamList[i]
                        duplicatedReg = possibility1 or possibility2
                        
                        if duplicatedReg == True:
                            break
                    if duplicatedReg == False:
                        drawList.append(list([teamList[j],None,teamList[i],None]))


    print('\n=================')
    print('New Draw Created!')
    print('=================\n')
    
    drawCreatedOnce = True
    drawCreatedFirst = True
    #Display the draw
    listDraw()

def addResult():
    #update the result of a match, hint use the enumerate function to identify which match to update
    while True:
        if drawCreatedOnce == False:
            print("\n*********************\n**  C A U T I O N  **\n*********************\nYou need to CREAT THE DRAW before listing the draw when\n      - Running the program at the first time\nOR    - Added new teams.\n")
            preAddResult = input('[Press ENTER to Acknowledge or Q to exit]')
            if preAddResult.upper() == 'Q':
                return print('Return menu. No new team added.')
        

        global drawList
        print("\n=== DRAW LIST ===\n")
        if drawList == []:
            print('*********************\n**  C A U T I O N  **\n*********************\nYou have not creat the draw!')
            return input('Press Enter to return to menu.')
        
        addResultCols = {'Index':int,'Team 1':str,'Score T1':int or bool,'Team 2':str, 'Score T2':int or bool}
        drawListDisplay = []
        # use enumerate to add the index to a temporary tuple 
        # so that user can choose the match
        for index,newList in enumerate(drawList):
            newList = drawList[index].copy()
            newList.insert(0,index)
            drawListDisplay.append(tuple(newList))
        columnOutput(drawListDisplay,addResultCols,"{0: ^7}|{1: ^20}|{2:^10}| VS |{4:^10}|{3: ^20}|")
        print('\n================\n')
        
        indexValidTrue = False
        while indexValidTrue == False:
            matchAddResultIndex = input('Please choose the match you are going to add results: ')
            if matchAddResultIndex.isnumeric() == False:
                print('*********************\n**  C A U T I O N  **\n*********************\nOnly numbers and valid index are allowed to be input!')
            else:
                if int(matchAddResultIndex) >= len(drawList):
                    print('*********************\n**  C A U T I O N  **\n*********************\nThis index is not available!')
                else:
                    break
        matchChosen = list(drawListDisplay[int(matchAddResultIndex)])

        for index,item in enumerate(matchChosen):
            if item == None:
                matchChosen[index] = ""
        
        print("{0: ^7}|{1: ^20}|{2:^10}| VS |{4:^10}|{3: ^20}|".format(*matchChosen))
        # Input the scores and store them into the drawList
        while True:
            matchScore1 = input(f'Please input the score of {drawListDisplay[int(matchAddResultIndex)][1]}: ')
            matchScore2 = input(f'Please input the score of {drawListDisplay[int(matchAddResultIndex)][3]}: ')
            if (matchScore1.isnumeric() == False) or (matchScore2.isnumeric() == False):
                print('*********************\n**  C A U T I O N  **\n*********************\nOnly numbers and valid index are allowed to be input!')
            else:
                if int(matchScore1) + int(matchScore2) != 5:
                    print('*********************\n**  C A U T I O N  **\n*********************\nThe total score should equal to 5!')
                else:
                    break
        
        drawList[int(matchAddResultIndex)][1] = int(matchScore1)
        drawList[int(matchAddResultIndex)][3] = int(matchScore2)
        matchResultAddOK = drawList[int(matchAddResultIndex)]
        
        print('\n=================')
        print('New Result Created!')
        print("|{0: ^20}|{1:^10}| VS |{3:^10}|{2: ^20}|".format(*matchResultAddOK))
        print('=================\n')
        
        sufAddResult = input('Input Q to return to menu or ENTER to add another results.')
        if sufAddResult.upper() == 'Q':
                break


# display the winner of matches
def displayWinners():
    if drawCreatedOnce == False:
        print("\n*********************\n**  C A U T I O N  **\n*********************\nYou need to CREAT THE DRAW before listing the draw when\n      - Running the program at the first time\nOR    - Added new teams.\n")
        preAddResult = input('[Press ENTER to Acknowledge or Q to exit]')
        if preAddResult.upper() == 'Q':
            return print('Return menu. No new team added.')
    

    global drawList
    print("\n=== Winners Display ===\n")
    if drawList == []:
        print('*********************\n**  C A U T I O N  **\n*********************\nYou have not creat the draw!')
        return input('Press Enter to return to menu.')
    
    addResultCols = {'WINNER':str,'Team 1':str,'Score T1':int or bool,'Team 2':str, 'Score T2':int or bool}
    drawListDisplay = []
# If results are None (results not added), display N/A, otherwise show the winner.
    for index,newList in enumerate(drawList):
        newList = drawList[index].copy()
        if (newList[1] == None) or (newList[3] == None) == True:
            winner = 'N/A'
        else:
            if newList[1] > newList[3]:
                winner = 'TEAM 1'
            else:
                winner = 'TEAM 2'
        newList.insert(0,winner)
        drawListDisplay.append(tuple(newList))
    columnOutput(drawListDisplay,addResultCols,"{0: ^10}|{1: ^20}|{2:^10}| VS |{4:^10}|{3: ^20}|")
    print('\n================\n')
    input('[Press ENTER to exit]')


#function to display the menu
def dispMenu():
    print("\n==== WELCOME TO LU TABLE TENNIS ====\n")
    print("1 - List Draw")
    print("2 - List Teams and Players")
    print("3 - List Players - alphabetical (by surname)")
    print("4 - List Players - alphabetical (by firstname)")
    print("5 - Add Team")
    print("6 - Add Match Result")
    print("7 - Create Draw")
    print("8 - Display Winners\n")
    print("R - Repeat the menu")
    print("Q - Quit\n")

#This is the main program

# Repeat this until user enters a "Q"
dispMenu()

response = input("Please select menu choice: ")
while response.upper() != "Q":
    if response == "1":
        listDraw()
    elif response == "2":
        listTeams()
    elif response == "3":
        listMembersSurnameAlpha()
    elif response == "4":
        listMembersFirstnameAlpha()
    elif response == "5":
        addTeam()
    elif response == "6":
        addResult()
    elif response == "7":
        createDraw()
    elif response == "8":
        displayWinners()
    elif response.upper() == "R":
        print("The menu has been repeated")
    else:
        print("invalid response, please re-enter")

    print("")
    dispMenu()
    response = input("Please select menu choice: ")

print("=== Thank you for using LU TABLE TENNIS ===")

