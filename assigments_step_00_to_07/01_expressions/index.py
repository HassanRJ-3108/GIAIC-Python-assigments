import random

DICE_NUMS = 6
def roll_dice():
    dice1 = random.randint(1,DICE_NUMS)
    dice2 = random.randint(1,DICE_NUMS)
    return dice1 + dice2

def main():
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()