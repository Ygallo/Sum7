# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#import pyinputplus as pyip

import pyfiglet
from colorama import Fore, Back, Style




def board_game():
    """
    Creates the board game with letter and number values for the player
    to choose the input its chip on its turn
    """
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(ROWS):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(COLS):
            if board[x][y] == "Yellow":
                print("", board[x][y], end="  |")
            elif board[x][y] == "Green":
                print("", board[x][y], end="  |")
            else:
                print(" ", board[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")


def ask_name():
    """
    Ask player name to add value to the dictionary
    and welcome player to th game
    """
    player1["name"] = input("Please enter your name player 1: \n")
    print("Welcome " + player1["name"])
    print("---------------------------------------------------\n")
    player2["name"] = input("Please enter your name player 2: \n")
    print("Welcome " + player2["name"])
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

# def checkIfCharacter(letter_choice):
    # """
    # Checking the value of the column selected by the player
    # to get the coordinate space to locate the chip
    # """
    # while True
    # try:
    # if choice in letter_choice:
    # pass


def is_space_available(column, row):
    """
    Checkin if there is space available in the board
    """
    print("checkin if column ", column, " row ", row, " is available")
    if board[column][row] == '1':
        return False
    elif board[column][row] == '2':
        return False
    elif board[column][row] == '3':
        return False
    else:
        return True


def check_gravity(column, chip):
    selected_column = coordinate_parser(column)
    print("selected_column", selected_column)
    for y in range(6, 0, -1):
        print("selected columns is: ", selected_column,  " y is: ", y)
        available = is_space_available(selected_column, y)
        #print(available, "available")
        if available:
            board[y][selected_column] = chip
            break
    board_game()
    # decide_turn()
    # select_play()


def select_play():
    current_player = None
    selected_column = None

    if player_turn == 1:
        current_player = player1
    else:
        current_player = player2

    selected_chip_input = input(
        current_player["name"] + " select a chip number from 1 to 3:   ")
    selected_chip = int(selected_chip_input)

    # validate_play(selected_chip)

    selected_column_input = input(
        current_player["name"] + " select a column from A to G:   ")
    selected_column = str(selected_column_input)
    print(selected_column)
    #check_gravity(selected_column, selected_chip)


# select_play()


def validate_play(chip):
    """
    Checks for valid input from the user
    """
    try:
        chip = int(chip)
        if chip > 3:
            raise ValueError(
            f"Only number from 1 to 3 are valid, you entered {chip}"
             )
        return True
    except ValueError as e:
        print( f"Invalid data: {e}, please try again. \n")
        return False 


def decide_turn():
    """
    Checking which player has a turn
    """
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1

def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL) 



if __name__ == "__main__":   
    print(validate_play("1"))
    print_red("Player 1 Ben")
    # print(board_game())
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
                  2, 2, 3, 3, 3, 3]
    }

    player2 = {
        "name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
                  2, 2, 2, 3, 3, 3, 3]
    }

    player_turn = 1

    board_game()
    ask_name()

