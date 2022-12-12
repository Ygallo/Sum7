# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#import pyinputplus as pyip

import pyfiglet
from colour import Color

yellow = Color("yellow")
print(yellow)

sum7 = pyfiglet.figlet_format("Welcome to Sum7", font = "bubble")
print(sum7)
print("Rules of the game:")
print("Players must add the same colored numbers in a row to win.")
print("Players share one board.")
print("Numbers go from 1 to 3.")
print("Only one number is played at a time.")
print("The game ends when a player sums 7 of the same color-in-a-row")
print("-------------------------------------------------------------")

letter_choice = ["A", "B", "C", "D", "E", "F", "G"]
board = [["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",], 
["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",], 
["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",], 
["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",]]
rows = 7
cols = 7

player1 = {
    	"name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 3, 3, 3, 3]
}

player2 = {
    	"name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 3, 3, 3, 3]
}


player_turn = 1

def board_game():
    """
    Creates the board game with letter and number values for the player
    to choose the input its chip on its turn
    """
    print("\n     A    B    C    D    E    F    G  ", end = "")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end ="")
        for y in range(cols):
            if (board[x][y] == "Yellow"):
                print("", board[x][y], end="  |")
            elif (board[x][y] == "Green"):
                print("", board[x][y], end="  |")
            else:
                print(" ", board[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")


def ask_name():
    """
    """
    player1["name"] = input("Please enter your name player 1: ")
    print("Welcome " + player1["name"])
    player2["name"] = input("Please enter your name player 2: ")
    print("Welcome " + player2["name"])

ask_name()


def isSpaceAvailable(column, row):
    print("checkin if column ", column, " row ", row, " is available")
    if (board[column][row] == '1'):
        return False
    elif (board[column][row] == '2'):
        return False
    elif (board[column][row] == '3'):
        return False  
    else:
        return True


def coordinateParser(inputString):
    print("inputString" + inputString)
    coordinate = 0
    if(inputString == "A"):
        coordinate = 0
    elif(inputString == "B"):
        coordinate = 1
    elif(inputString == "C"):
        coordinate = 2
    elif(inputString == "D"):
        coordinate = 3
    elif(inputString == "E"):
        coordinate = 4
    elif(inputString == "F"):
        coordinate = 5
    elif(inputString == "G"):
        coordinate = 6
    else:
        print("Invalid")
    print(coordinate)
    return coordinate

def select_play():
    current_player = None
    selected_column = None

    if player_turn == 1:
        current_player = player1
    else:
        current_player = player2
    
    selected_chip_input = input(" Select a chip number from 1 to 3:   ")
    selected_chip = int(selected_chip_input)

    selected_column_input  = input(" Select a column from A to G:   ")
    selected_column = str(selected_column_input)
    print(selected_column)
    check_gravity(selected_column, selected_chip)


select_play()


def decide_turn():
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1


def check_gravity(column, chip):
    selected_column = coordinateParser(column)
    print("selected_column", selected_column)
    for y in range(6, 0, -1):
        print("selected columns is: ", selected_column,  " y is: ", y)
        available = isSpaceAvailable(selected_column, y)
        #print(available, "available")
        if (available == True):
            board[y][selected_column] = chip
            break
    board_game()
    decide_turn()
    select_play()




#print(board_game())

