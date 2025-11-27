import random
def treasure_hunt():
    found_treasure = False
    size = int(input("enter the size of the board: "))
    treasure_row = random.randint(1, size)
    treasure_col = random.randint(1, size)
    print("the game started, try finding the treasure!")
    print(f"the board size is: {size}x{size}.")
    while found_treasure != False:
        guess_row = int(input("guess the row: "))
        guess_col = int(input("guess the column: "))
        if guess_row == treasure_row and guess_col == treasure_col:
            print("good for you! you found the treasure!")
            found_treasure = True
        if guess_row < treasure_row:
            print("go a bit more down")
        elif guess_row > treasure_row:
            print("go a bit more up")
        if guess_col < treasure_col:
            print("go a bit more right")
        elif guess_col > treasure_col:
            print("go a bit more left")
        print("---")


treasure_hunt()
