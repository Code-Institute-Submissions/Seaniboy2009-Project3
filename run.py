# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


class Board:
    """
    Create instance of the board class
    """
    def __init__(self, name, size, ships):
        self.name = name
        self.size = size
        self.board = [["[]" for x in range(size)] for y in range(size)]
        self.ships = ships


def validate_input(input):
    """
    Checkes the input and validates it as int and sting or out of scope
    """
    valid_input = [4, 5, 6, 7, 8]
    try:
        if int(input) not in valid_input:
            raise ValueError(
                f"Must be {valid_input}, you put {input}"
            )       
    except ValueError as e:
        print(f"input is invalid {e}, please try again")
        return False

    return True


def start_game():
    """
    Initialize the start function, ask for player name, board size.
    """

    print('Welcome to battleships, please have fun and remember to shout:')
    print('"YOU SUNK MY BATTLESHIP"\n')

    name = input("Please enter your name:\n")

    while True:

        size = int(input("Please pick board size, from 4x4 min to 8x8 max:\n"))
        if validate_input(size):
            break

    while True:

        ships = input("Please select number of ships, 2 min 6 max")
        if validate_input(ships):
            break

    player_b = Board(name, size, ships)
    computer_b = Board("Computer", size, ships)


start_game()
