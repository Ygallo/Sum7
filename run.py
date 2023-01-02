# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from itertools import groupby
import os
import pyfiglet
from colorama import Fore, Back, Style
import pyinputplus as pyip

# code taken from connect4 tutorial


def board_game():
    """
    Creates the board game with letter and number values for the players
    to choose the where to locate its chip on each turn
    """
    print("\n      A     B     C     D     E     F     G  ", end="")
    for x in range(ROWS):
        print("\n   +-----+-----+-----+-----+-----+-----+-----+")
        print(x, " |", end="")
        for y in range(COLS):
            if chip_owner[x][y] == "player1":
                print("", Fore.YELLOW +
                      str(board[x][y]) + Style.RESET_ALL, end="   |")
            elif chip_owner[x][y] == "player2":
                print("", Fore.GREEN +
                      str(board[x][y]) + Style.RESET_ALL, end="   |")
            else:
                print(" ",  board[x][y], end="   |")
    print("\n   +-----+-----+-----+-----+-----+-----+-----+")


def ask_name():
    """
    Ask players name, assigns a color to each player
    and welcome players to the game
    """
    player1["name"] = pyip.inputStr("Please enter your name player 1: \n")
    print("Welcome " + Fore.YELLOW + player1["name"].upper() + Style.RESET_ALL)
    print("---------------------------------------------------\n")
    player2["name"] = pyip.inputStr("Please enter your name player 2: \n")
    print("Welcome " + Fore.GREEN + player2["name"].upper() + Style.RESET_ALL)
    print("---------------------------------------------------\n")

# code taken from connect4 tutorial


def coordinate_parser(input_string):
    """
    Checking the value of the column selected by the player
    to get the coordinate space to locate the chip on the board
    """
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
    return coordinate


def is_space_available(column, row):
    """
    Checkin if there is space available on the board
    """
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
    as if there was gravity and occupy space available on the board.
    Print the board with the new played chip and check if there are any
    vertical or horizontal sum7. If no winner, will continue with the
    next turn.
    """

    selected_column = coordinate_parser(column)
    current_turn = check_turn()

    for y in range(6, -1, -1):
        available = is_space_available(y, selected_column)

        if available:
            board[y][selected_column] = chip
            remove_played_chip(current_player, chip)
            chip_owner[y][selected_column] = current_turn
            break
        elif not available and y == 0:
            print("That space is taken, choose another column")
            select_play()

    board_game()
    board_full()

    for boardx in board:
        winner = check_horizontal(board[y], chip_owner[y])
        if winner:
            end_game(current_player)
            break

    column_array = []
    for boardy in board:
        resulty = convert_column(boardy, selected_column)
        column_array.append(resulty)

    chip_owner_array = []
    for chipy in chip_owner:
        result_owner = convert_column(chipy, selected_column)
        chip_owner_array.append(result_owner)

    column_array_reversed = column_array[::-1]
    chip_owner_array_reversed = chip_owner_array[::-1]

    for boardy in column_array:
        winner = check_vertical_winners(
            column_array_reversed, chip_owner_array_reversed)
        if winner:
            end_game(current_player)
            break

    decide_turn()
    select_play()


def convert_column(column, selected_column):
    """
    Converts the columns of the matrix in an array,
    for evaluation of sums later.
    """
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
                                        current_player["name"].upper() +
                                        Style.RESET_ALL +
                                        " select one of your chips:   \n")

    selected_chip = int(selected_chip_input)

    validate_number(selected_chip, current_player)

    selected_column_input = pyip.inputMenu(["A", "B", "C", "D", "E", "F", "G"],
                                           prompt=current_player["color"] +
                                           current_player["name"].upper()
                                           + Style.RESET_ALL +
                                           " select a column from A to G:  \n")

    selected_column = str(selected_column_input)
    check_gravity(selected_column, selected_chip, current_player)


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
    Removes the played chip from available chips of each player.
    Used chip cannot be used again.
    """

    chips = player["chips"]
    for i in chips:
        if i == selected_chip:
            chips.remove(i)
            break


def board_full():
    """
    If there are no winners and the board is full,
    reset the game.
    """
    counter = 0

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] != "":
                counter += 1

    if counter == 49:
        print(pyfiglet.figlet_format("Sorry, no winners", font="bubble"))
        play_again = pyip.inputMenu(
            ["Yes", "No"], prompt="Would you like to play again: \n")

        if play_again == "Yes":
            reset_game()

        else:
            os.system('clear')
            print(pyfiglet.figlet_format("Thank you for playing",
                                         font="bubble"))
            exit()


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


def all_equal(iterable):
    """
    Checks if it is the same owner of the chip
    to sum them up
    """
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
                return True

    return False


def check_vertical_winners(column, chip_owner):
    """
    Checks for winner on a vertical column, checks that a min of 3 chips
    of the same player are in a column to win
    """

    for minimum_chips_for_win in range(3, 8):
        for index, chip in enumerate(column):

            if chip == "":
                continue
            chips_to_sum = []
            chips_to_sum_owners = []
            for chip_index in range(minimum_chips_for_win):
                if index + chip_index > 6:
                    break
                chips_to_sum.append(column[index + chip_index])
                chips_to_sum_owners.append(chip_owner[index + chip_index])
            if not all_equal(chips_to_sum_owners):
                continue
            chips_to_sum = string_list_to_int_list(chips_to_sum)
            if None in chips_to_sum:
                continue
            chip_sum = sum(chips_to_sum)
            if chip_sum == 7:
                return True
    return False


def reset_game():
    """
    If game is over, resets the game to new, clearing the board,
    setting all the available chips to play again.
    """

    for i in range(ROWS):
        for j in range(COLS):
            board[i][j] = ""
            chip_owner[i][j] = ""

    player1["name"] = ""
    player1["chips"] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
    player2["turn"] = True

    player2["name"] = ""
    player2["chips"] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
    player2["turn"] = False

    os.system('clear')
    board_game()
    ask_name()
    select_play()


def end_game(current_player):
    """
    Once a winner is found, congratulate the player and
    ask if the wish to play again. If yes, reset the game,
    if no end game, and thanks for playing.
    """
    print(pyfiglet.figlet_format("Congratulations ", font="bubble"))
    print(current_player["color"] +
          current_player["name"].center(40) + Style.RESET_ALL)
    print(pyfiglet.figlet_format(" You won the game", font="bubble"))
    play_again = pyip.inputMenu(
        ["Yes", "No"], prompt="Would you like to play again: \n")

    if play_again == "Yes":
        reset_game()

    else:
        os.system('clear')
        print(pyfiglet.figlet_format("Thank you for playing", font="bubble"))
        print()
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

    sum7 = pyfiglet.figlet_format("Welcome to Sum7", font="bubble")
    print(sum7)
    print("Rules of the game:")
    print("-------------------------------------------------------------")
    print("Players must add the same colored numbers in a row/column to win.")
    print("Players share one board.")
    print("Numbers go from 1 to 3.")
    print("Only one number is played at a time.")
    print("The game ends when a player sums 7")
    print("-------------------------------------------------------------")

    letter_choice = ["A", "B", "C", "D", "E", "F", "G"]
    board = [["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""]]

    chip_owner = [["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""]]

    ROWS = 7
    COLS = 7

    minimum_chips_for_win = 3

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

    board_game()
    ask_name()
    select_play()
