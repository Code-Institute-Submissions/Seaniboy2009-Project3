# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start_game():
    """
    Initialize the start function, ask for player name, board size.
    """

    print('Welcome to battleships, please have fun and remember to shout:')
    print('"YOU SUNK MY BATTLESHIP"\n')

    name = input("Please enter your name:\n")
    print(name)
    b_size = input("Please pick board size, from 4x4 min to 8x8 max:\n")
    print(b_size)


start_game()
