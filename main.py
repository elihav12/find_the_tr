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
