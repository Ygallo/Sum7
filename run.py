# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet
from colorama import Fore, Back, Style
import pyinputplus as pyip
from itertools import groupby
import numpy as np

#turn = 2


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
                print("", Fore.YELLOW +
                      str(board[x][y]) + Style.RESET_ALL, end="   |")
            elif chipOwner[x][y] == "player2":
                print("", Fore.GREEN +
                      str(board[x][y]) + Style.RESET_ALL, end="   |")
            else:
                print(" ",  board[x][y], end="   |")
    print("\n   +-----+-----+-----+-----+-----+-----+-----+")


def ask_name():
    """
    Ask player name to add value to the dictionary
    and welcome player to the game
    """
    player1["name"] = pyip.inputStr("Please enter your name player 1: \n")
    print("Welcome " + Fore.YELLOW + player1["name"].upper() + Style.RESET_ALL)
    print("---------------------------------------------------\n")
    player2["name"] = pyip.inputStr("Please enter your name player 2: \n")
    print("Welcome " + Fore.GREEN + player2["name"].upper() + Style.RESET_ALL)
    print("---------------------------------------------------\n")


def coordinate_parser(input_string):
    """
    Checking the value of the column selected by the player
    to get the coordinate space to locate the chip on the board
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
    Checkin if there is space available on the board
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


def check_gravity(column, chip, current_player):
    """
    Check the player chip location on the board. Chips must fall
    as if there was gravity and occupy space available on the board
    """
    selected_column = coordinate_parser(column)
    #print("selected_column", selected_column)
    current_turn = check_turn()

    for y in range(6, 0, -1):
        #print("selected columns is: ", selected_column,  " y is: ", y)
        available = is_space_available(y, selected_column)
        #print(available, "available")
        if available:
            board[y][selected_column] = chip
            chipOwner[y][selected_column] = current_turn
            break
    board_game()
    # check_winner(current_turn)
    # check_horizontal_winners(selected_column)

    for boardx in board:
        winner = check_horizontal(board[y], chipOwner[y])
        if winner:
            end_game(current_player)
            break

    column_array = []
    for boardy in board:
        resulty = convert_column(boardy, selected_column)
        column_array.append(resulty)

    column_array_reversed = column_array[::-1]
    chipOwner_array = []
    for chipy in chipOwner:
        result_owner = convert_column(chipy, selected_column)
        chipOwner_array.append(result_owner)

    chipOwner_array_reversed = chipOwner_array[::-1]

    for boardy in column_array:
        winner = check_vertical_winners(
            column_array_reversed, chipOwner_array_reversed)
        if winner:
            end_game(current_player)
            break

    decide_turn()
    select_play()


def convert_column(column, selected_column):
    for position, value in enumerate(column):
        if position == selected_column:
            return value


def select_play():
    """
    Checks whos turn is on the game. Ask the player to choose a chip
    from the ones available, and validates that the chip has not been used.
    Ask the player to choose a column for the chosen chip and prints
    the board with the played chip.
    """
    current_player = None
    selected_column = None

    if player1["turn"]:
        current_player = player1
    else:
        current_player = player2

    print("This are the chips you have available: ",
          current_player["color"] + str(current_player["chips"]) +
          Style.RESET_ALL)

    selected_chip_input = pyip.inputNum(current_player["color"] +
                                        current_player["name"].upper() + Style.RESET_ALL +
                                        " select one of your chips:   ")

    selected_chip = int(selected_chip_input)

    validate_number(selected_chip, current_player)
    # current_player["chip"]
    remove_played_chip(current_player, selected_chip)

    selected_column_input = pyip.inputMenu(["A", "B", "C", "D", "E", "F", "G"],
                                           prompt=current_player["color"] +
                                           current_player["name"].upper() + Style.RESET_ALL +
                                           " select a column from A to G:   \n")

    selected_column = str(selected_column_input)
    # print(selected_column)
    check_gravity(selected_column, selected_chip, current_player)


# select_play()


def validate_number(chip, current_player):
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
                f"You dont have that {chip} available"
            )
        elif chip <= 3 and result > 0:
            return True
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        select_play()


def remove_played_chip(player, selected_chip):
    """
    Removes the played chip form the dictionary.
    Used chip cannot be used again.
    """

    chips = player["chips"]
    for i in chips:
        if i == selected_chip:
            chips.remove(i)
            break


def check_turn():
    """
    Return who is playing.
    """
    if player1["turn"]:
        return "player1"
    else:
        return "player2"


def decide_turn():
    """
    Checking which player has a turn
    """
    if player1["turn"] is True:
        player1["turn"] = False
        player2["turn"] = True
    else:
        player2["turn"] = False
        player1["turn"] = True


minimum_chips_for_win = 3


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def string_list_to_int_list(string_list):
    """
    Transforms the chips into interger, and appends to a new list
    to sum the players chip to calculate the sum 7
    """
    int_list = []
    for item in string_list:
        if item == "":
            int_list.append(None)
        else:
            int_list.append(int(item))
    return int_list


def check_horizontal(row, owners_row):
    """
    Checks for winner on horizontal row, checks that a min of 3 chips
    of the same player are in row
    """
    for minimum_chips_for_win in range(3, 8):
        for index, chip in enumerate(row):
            # print(index, chip)
            if chip == "":
                continue
            chips_to_sum = []
            chips_to_sum_owners = []
            for chip_index in range(minimum_chips_for_win):
                if index + chip_index > 6:
                    break
                chips_to_sum.append(row[index + chip_index])
                chips_to_sum_owners.append(owners_row[index + chip_index])
            if not all_equal(chips_to_sum_owners):
                chips_to_sum = []
                continue
            chips_to_sum = string_list_to_int_list(chips_to_sum)
            if None in chips_to_sum:
                continue
            chip_sum = sum(chips_to_sum)
            if chip_sum == 7:
                #print("Winner found")
                return True
                # break
    #print("No winner found!")
    return False


def check_horizontal_winners(row):
    """
    Checks for winner on horizontal row, checks that a min of 3 chips
    of the same player are in row
    """
    for minimum_chips_for_win in range(3, 8):
        for index, chip in enumerate(row):
            # print(index, chip)
            if chip == "":
                continue
            chips_to_sum = []
            chips_to_sum_owners = []
            for chip_index in range(minimum_chips_for_win):
                if index + chip_index > 6:
                    break
                chips_to_sum.append(row[index + chip_index])
                chips_to_sum_owners.append(chipOwner[index + chip_index])
            if not all_equal(chips_to_sum_owners):
                del chips_to_sum
                continue
            chips_to_sum = string_list_to_int_list(chips_to_sum)
            if None in chips_to_sum:
                continue
            chip_sum = sum(chips_to_sum)
            if chip_sum == 7:
                #print("Winner found")
                return True
                # break
    #print("No winner found!")
    return False


def check_vertical_winners(column, chipOwner):
    """
    Checks for winner on a vertical column, checks that a min of 3 chips
    of the same player are in a column to win
    """

    for minimum_chips_for_win in range(3, 8):
        for index, chip in enumerate(column):
            # print(index, chip)
            if chip == "":
                continue
            chips_to_sum = []
            chips_to_sum_owners = []
            for chip_index in range(minimum_chips_for_win):
                if index + chip_index > 6:
                    break
                chips_to_sum.append(column[index + chip_index])
                chips_to_sum_owners.append(chipOwner[index + chip_index])
            if not all_equal(chips_to_sum_owners):
                continue
            chips_to_sum = string_list_to_int_list(chips_to_sum)
            if None in chips_to_sum:
                continue
            chip_sum = sum(chips_to_sum)
            if chip_sum == 7:
                #print("Winner found")
                return True
                # break
    #print("No winner found!")
    return False


def end_game(current_player):
    print(pyfiglet.figlet_format("Congratulations ", font="bubble"))
    print(current_player["color"] + current_player["name"].upper() + Style.RESET_ALL)
    print(pyfiglet.figlet_format(" You won the game", font="bubble"))
    play_again = pyip.inputYesNo(prompt="Would you like to play again: ")
    
    if play_again == "Yes":
        #print("Yes")
        board_game()
        ask_name()
        select_play()
    else:
        exit()


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

    # select_play()
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
    board = [["", "", "", "", "", "", "",],
             ["", "", "", "", "", "", "",],
             ["", "", "", "", "", "", "",],
             ["", "", "", "", "", "", "",],
             ["", "", "", "", "", "", "",],
             ["", "", "", "", "", "", "",],
             ["", "", "", "", "", "", "",]]

    '''board = [["", "", "", "", "", "", "",],
    ["", "", "", "", "", "", "",],
    ["", "", "", "", "", "", "",], 
    ["", "", "", "", "", "", "",],
    [2, "", "", "", "", "", "",], 
    [3, "", "", "", "", "", "",],
    [3, 2, 1, 3, 2, "", "",]]'''

    '''chipOwner = [["", "", "", "", "", "", "",],
    ["", "", "", "", "", "", "",],
    ["", "", "", "", "", "", "",], 
    ["", "", "", "", "", "", "",],
    ["player1", "", "", "", "", "", "",], 
    ["player1", "", "", "", "", "", "",],
    ["player1", "player2", "player2", "player2", "player1", "", "",]]'''

    chipOwner = [["", "", "", "", "", "", "",],
                 ["", "", "", "", "", "", "",],
                 ["", "", "", "", "", "", "",],
                 ["", "", "", "", "", "", "",],
                 ["", "", "", "", "", "", "",],
                 ["", "", "", "", "", "", "",],
                 ["", "", "", "", "", "", "",]]

    ROWS = 7
    COLS = 7

    won = False

    player1 = {
        "name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                  2, 2, 3, 3, 3, 3],
        "turn": True,
        "color": Fore.YELLOW
    }

    player2 = {
        "name": "",
        "chips": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
                  2, 2, 2, 3, 3, 3, 3],
        "turn": False,
        "color": Fore.GREEN
    }

    turn = 2


    board_game()
    ask_name()
    select_play()
   # decide_turn()
