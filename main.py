import random

def create_board(size):
    return [["." for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


