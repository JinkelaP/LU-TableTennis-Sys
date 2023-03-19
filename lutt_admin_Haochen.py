##############################  LU TABLE TENNIS ADMINISTRATION  ###############################
### Name:   Haochen Zhu
### Student ID: 
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
    # Print out a copy of the draw
    
    input("\nPress Enter to continue.")     # End function with this line

def listTeams():
    # Print a list of the teams
    displayList = []
    for team in dbTeams.keys():
        displayList.append((team,f'{dbTeams[team][0][0]} {dbTeams[team][0][1]}',f'{dbTeams[team][1][0]} {dbTeams[team][1][1]}'))
    print("\nALL TEAMS\n")
    columnOutput(displayList,colTeams,"|{: <15} |{: <15} |{: <15}|") #example of how to call columnOutput function
    
    
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
    colNames = {'Firstname': str, 'Surname': str}
    columnOutput(sortedPlayers,colNames,"|{: <11} |{: <11}|")
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
    colNames = {'Firstname': str, 'Surname': str}
    columnOutput(sortedPlayers,colNames,"|{: <11} |{: <11}|")
    input("\nPress Enter to continue.")     # End function with this line

def addTeam():
    # add a team. Check a Player does not already exist.
    # Generate the team name and check that it does not already exist
    # Team Name is First Surname and Second Surname joined together each with an initial capital letter
    print('================')
    #Function of checking if the player has already been registered in the other team
    def nameCheck(newNameTuple):
        playerList = []
        for team in dbTeams.keys():
            playerList.append(dbTeams[team][0])
            playerList.append(dbTeams[team][1])
        
        for names in playerList:
            if newNameTuple == names:
                return True
        return False
    

    # Registering the first new player
    while True:
        newFirstname1 = str(input('Please type the firstname of player 1: ')).casefold().capitalize()
        newSurname1 = str(input('Please type the Surname of player 1: ')).casefold().capitalize()
        newName1Tuple = tuple((newFirstname1,newSurname1))
        
        if newFirstname1.isnumeric() == True or newSurname1.isnumeric() == True:
            nameCheckFail = str(input("==========\n**CAUTION**\nThe player's name cannot contain numbers only. \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select:"))
            if nameCheckFail.upper() == 'Q':
                return print('Return menu. No new team added.')
        
        else:
            break
        
        
        # If the player has been registered, the admin can either input a new name or leave the addTeam function
    while True:   
        if nameCheck(newName1Tuple) == True:
            nameCheckFail = str(input('==========\n**CAUTION**\nThe player has been registered into another team! \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select:'))
            if nameCheckFail.upper() == 'Q':
                return print('Return menu. No new team added.')
                
        else:
            print('Player 1 name check PASSED.\n')
            break

    while True:
        newFirstname2 = str(input('Please type the firstname of player 2: ')).casefold().capitalize()
        newSurname2 = str(input('Please type the Surname of player 2: ')).casefold().capitalize()
        newName2Tuple = tuple((newFirstname2,newSurname2))
        # If the player has been registered in other teams or in the player 1, the admin can either input a new name or leave the addTeam function
        if nameCheck(newName2Tuple) == True:
            nameCheckFail = str(input('==========\n****CAUTION****\nThe player has been registered into another team! \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select:'))
            if nameCheckFail.upper() == 'Q':
                return print('Return menu. No new team added.')
        elif newName1Tuple == newName2Tuple:
            nameCheckFail = str(input('==========\n****CAUTION****\nThe player name has been input as player 1! \nPress Enter to input a new name or enter Q to return to the menu.\nPlease select:'))
            if nameCheckFail.upper() == 'Q':
                return print('Return menu. No new team added.')
        else:
            print('Player 2 name check PASSED.\n')
            break
    
    newTeamName = newSurname1 + newSurname2
    
    # Check if teamName is unique
    teamNameCheck = None
    teamNameCheckResult = None
    while True:
        for key in dbTeams.keys():
            if newTeamName.upper() == key.upper():
                teamNameCheckResult = True
                print("Sorry, the auto-generated team name '{}' has been registered in the database.".format(newTeamName))
                break
            else:
                teamNameCheckResult = False
        
        if teamNameCheckResult == False:
            print('Team name check PASSED.\n')
            break
        elif teamNameCheckResult == True:
            newTeamName = str(input("Please create a different team name: "))
    
    
    # Add new team to the dictionary
    dbTeams[newTeamName] = [newName1Tuple,newName2Tuple]

    print(f"Congrats! The team has been registered succesfully.\nTeam: {newTeamName}\nPlayer1: {newFirstname1} {newSurname1}\nPlayer2: {newFirstname2} {newSurname2}")
    input('======\nPress Enter to return to menu.')




def createDraw():
    #each team should play each other team, but only once.

    #Display the draw
    listDraw()

def addResult():
    #update the result of a match, hint use the enumerate function to identify which match to update
    pass




#function to display the menu
def dispMenu():
    print("==== WELCOME TO LU TABLE TENNIS ====")
    print("1 - List Draw")
    print("2 - List Teams and Players")
    print("3 - List Players - alphabetical (by surname)")
    print("4 - List Players - alphabetical (by firstname)")
    print("5 - Add Team")
    print("6 - Add Match Result")
    print("7 - Create Draw")
    print("R - Repeat the menu")
    print("Q - Quit")

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
    elif response.upper() == "R":
        print("The menu has been repeated")
    else:
        print("invalid response, please re-enter")

    print("")
    dispMenu()
    response = input("Please select menu choice: ")

print("=== Thank you for using LU TABLE TENNIS ===")

