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

letter_choice = ["A", "B", "C", "D", "E", "F", "G"]
board = [["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",], 
["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",], 
["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",], 
["", "", "", "", "", "", "",], ["", "", "", "", "", "", "",]]
rows = 7
cols = 7


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


print(board_game())
