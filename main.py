import random

def create_board(size):
    return [["." for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
def get_input(prompt, size):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= size:
                return value
            else:
                print(f"the gase has to be between 1 to: {size}.")
        except ValueError:
            print("it has to be a number")
def treasure_hunt():
    size = int(input("Enter board size: "))
    attempts_limit = int(input("Enter max number of attempts: "))

    board = create_board(size)

    treasure_row = random.randint(1, size)
    treasure_col = random.randint(1, size)

    print("\nThe game has started! Try finding the treasure!")
    print(f"Board size: {size}x{size}")
    print()

    attempts = 0

    while attempts < attempts_limit:
        print_board(board)

        guess_row = get_input("Guess row: ", size)
        guess_col = get_input("Guess column: ", size)
        attempts += 1

        if board[guess_row - 1][guess_col - 1] == "X":
            print("you all ready tried this one")
            continue

        board[guess_row - 1][guess_col - 1] = "X"

        if guess_row == treasure_row and guess_col == treasure_col:
            print("\ngood job, you win!")
            print(f"you did it in {attempts} try")
            return

        if guess_row < treasure_row:
            print("go a bit down")
        elif guess_row > treasure_row:
            print("go a bit up")

        if guess_col < treasure_col:
            print("go a bit right")
        elif guess_col > treasure_col:
            print("go a bit left")

        print(f"Attempts left: {attempts_limit - attempts}")
        print("---")

    print("\nyour out of attempts")
    print(f"the treasure was in row {treasure_row}, line {treasure_col}.")


treasure_hunt()
