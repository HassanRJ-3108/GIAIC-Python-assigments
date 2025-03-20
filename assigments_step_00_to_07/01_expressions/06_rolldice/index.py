import random

DIE_FACE = 6 # Number of each die to roll

def roll_dice():
    # Roll die
    die1 = random.randint(1, DIE_FACE)
    die2 = random.randint(1, DIE_FACE)
    
    return die1, die2 # returning both dies value
                         
def main():
    die1, die2 = roll_dice() # Extract dies values

    print("Die 1 is:", die1) # Print die 1
    print("Die 2 is:", die2) # Print die 2
    print("Total of these dies are:", die1 + die2) # Their total

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()