from random import randint


class Board:
    """
    Create instance of the board class
    """
    def __init__(self, name, size, num_ships, type):
        self.name = name
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.type = type
        self.ships = []
        self.misses = []

    def create_board(self):
        for row in self.board:
            print(" ".join(row))

    def add_ship(self, x, y):
        self.ships.append((x, y))
        self.board[x][y] = "!"
        # if self.type == "player":
        #     self.board[x][y] = "!"
        print(self.ships)

    # def take_shot(self, x, y):
    #     if self.board[x][y]


def validate_input(input):
    """
    Checkes the input and validates it as int and sting or out of scope
    """
    valid_input = [4, 5, 6, 7, 8]
    try:
        if input not in valid_input:
            raise ValueError(
                f"Must be {valid_input}, you put {input}"
            )       
    except ValueError as e:
        print(f"input is invalid {e}, please try again")
        return False

    return True


def add_ships_to_board(board):
    """
    Add player and computer ships to there boards using random.
    """
    num1 = return_num(board.size)
    num2 = return_num(board.size)
    board.add_ship(num1, num2)


def return_num(num):
    """
    Returns a random number within the num and 0
    """

    return randint(0, num - 1)


def start_game():
    """
    Initialize the start function, ask for player name, board size.
    """

    print('Welcome to battleships, please have fun and remember to shout:')
    print('"YOU SUNK MY BATTLESHIP"\n')

    # Testing
    name = "Player"
    size = 2
    ships = 2

    # name = input("Please enter your name:\n")

    # while True:

    #     size = int(input("Please pick board size, Min 4: Max 8:\n"))
    #     if validate_input(size):
    #         break

    # while True:

    #     ships = int(input("Please select number of ships, Min 4: Max 8:\n"))
    #     if validate_input(ships):
    #         break

    player_b = Board(name, size, ships, "player")
    computer_b = Board("Computer", size, ships, "computer")

    for ship in range(ships):
        add_ships_to_board(player_b)
        add_ships_to_board(computer_b)

    player_b.create_board()
    print("_" * (size * size))
    computer_b.create_board()


start_game()
