# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#import pyinputplus as pyip

import pyfiglet

sum7 = pyfiglet.figlet_format("Welcome to Sum7", font = "bubble")
print(sum7)
print("Rules of the game:")
print("Players must add the same colored numbers in a row to win.")
print("Players share one board.")
print("Numbers go from 1 to 3.")
print("Only one number is played at a time.")
print("The game ends when a player sums 7 of the same color-in-a-row")