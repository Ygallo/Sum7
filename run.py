# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet
from colorama import Fore, Back, Style
import pyinputplus as pyip

ROWS = 7
COLS = 7

board = [["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",],
         ["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",],
         ["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",],
         ["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",]]

chipOwner = [["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",],
         ["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",],
         ["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",],
         ["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",]]



turn = 1


def board_game():
    """
    Creates the board game with letter and number values for the player
    to choose the input its chip on its turn
    """
    print("\n      A     B     C     D     E     F     G  ", end="")
    for x in range(ROWS):
        print("\n   +-----+-----+-----+-----+-----+-----+-----+")
        print(x, " |", end="")
        for y in range(COLS):
            if chipOwner[x][y] == "player1":
                print("", Fore.YELLOW + str(board[x][y]) + Style.RESET_ALL, end="   |")
            elif chipOwner[x][y] == "player2":
                print("", Fore.GREEN + str(board[x][y]) + Style.RESET_ALL, end="   |")
            else:
                print(" ",  board[x][y], end="   |")           
    print("\n   +-----+-----+-----+-----+-----+-----+-----+")


def ask_name():
    """
    Ask player name to add value to the dictionary
    and welcome player to th game
    """
    #player1["name"] = input("Please enter your name player 1: \n")
    player1["name"]= pyip.inputStr("Please enter your name player 1: \n")
    print("Welcome " + Fore.YELLOW + player1["name"] + Style.RESET_ALL)
    print("---------------------------------------------------\n")
    player2["name"] = pyip.inputStr("Please enter your name player 2: \n")
    print("Welcome " + Fore.GREEN + player2["name"] + Style.RESET_ALL)
    print("---------------------------------------------------\n")


def coordinate_parser(input_string):
    """
    Checking the value of the column selected by the player
    to get the coordinate space to locate the chip
    """
    print("input_string" + input_string)
    coordinate = 0
    if input_string == "A":
        coordinate = 0
    elif input_string == "B":
        coordinate = 1
    elif input_string == "C":
        coordinate = 2
    elif input_string == "D":
        coordinate = 3
    elif input_string == "E":
        coordinate = 4
    elif input_string == "F":
        coordinate = 5
    elif input_string == "G":
        coordinate = 6
    else:
        print("Invalid")
    print(coordinate)
    return coordinate


def is_space_available(column, row):
    """
    Checkin if there is space available in the board
    """
    print("checkin if column ", column, " row ", row, " is available")
    print("current value of the position", board[column][row])
    if board[column][row] == 1:
        return False
    elif board[column][row] == 2:
        return False
    elif board[column][row] == 3:
        return False
    else:
        return True


def check_gravity(column, chip):
    selected_column = coordinate_parser(column)
    print("selected_column", selected_column)
    current_turn=check_turn()

    for y in range(6, 0, -1):
        print("selected columns is: ", selected_column,  " y is: ", y)
        available = is_space_available(y, selected_column)
        print(available, "available")
        if available:
            board[y][selected_column] = chip
            chipOwner[y][selected_column]=current_turn
            break
    board_game()
    decide_turn()
    select_play()


def select_play():
    current_player = None
    selected_column = None


    if player1["turn"]:
        current_player = player1
    else:
        current_player = player2

    print("This are the chips you have available: ", current_player["color"] + str(current_player["chips"]) + Style.RESET_ALL)
    selected_chip_input = input(current_player["color"] +
        current_player["name"] + Style.RESET_ALL + " select one of your chips:   ")
    selected_chip = int(selected_chip_input)

    validate_number(selected_chip,current_player)
    #current_player["chip"]
    remove_played_chip(current_player,selected_chip)

    selected_column_input = pyip.inputMenu(["A", "B", "C", "D", "E", "F", "G"], prompt =
        current_player["color"] + current_player["name"] + Style.RESET_ALL + " select a column from A to G:   \n")
    selected_column = str(selected_column_input)
    print(selected_column)
    check_gravity(selected_column, selected_chip)


#select_play()


def validate_number(chip,current_player):
    """
    Checks for valid number input from the user
    """
    chips = current_player["chips"]
    try:
        chip = int(chip)
        result = chips.count(chip)
        if chip > 3:
            raise ValueError(
                f"You entered {chip}"
            )
        elif chip <= 3 and result == 0:
            raise ValueError(
                f"You dont have that {chip}"
            )
        elif chip <= 3 and result > 0:    
            return True
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        select_play()


def remove_played_chip(player,selected_chip):
    
    chips=player["chips"]
    for i in chips:
        if i == selected_chip:
            chips.remove(i)
            break
    

def check_turn():
    """
    return who is playing
    """
    if player1["turn"]:
        return "player1"
    else:
        return "player2"

def decide_turn():
    """
    Checking which player has a turn
    """
    if player1["turn"] == True:
        player1["turn"] = False
        player2["turn"] = True
    else:
        player2["turn"] = False
        player1["turn"] = True


def print_yellow(text):
    """
    Change the color to yellow for player 1 input on the board
    """
    print(Fore.YELLOW + text + Style.RESET_ALL, end="")



def print_green(text):
    """
    Change the color to green for player 2 input on the board
    """
    print(Fore.GREEN + text + Style.RESET_ALL)


if __name__ == "__main__":

    #print(validate_letter("M"))
    #select_play()
    #print_yellow("Player 1 Ben")
    sum7 = pyfiglet.figlet_format("Welcome to Sum7", font="bubble")
    print(sum7)
    print("Rules of the game:")
    print("-------------------------------------------------------------")
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
    ROWS = 7
    COLS = 7

    player1 = {
        "name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                  2, 2, 3, 3, 3, 3],
        "turn": False,
        "color": Fore.YELLOW
    }

    player2 = {
        "name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
                  2, 2, 2, 3, 3, 3, 3],
        "turn": False,
        "color":Fore.GREEN
    }

    #turn = 1

    board_game()
    ask_name()
    select_play()
   #decide_turn()
