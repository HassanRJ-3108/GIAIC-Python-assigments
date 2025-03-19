# Problem Statement

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1. Prompt the user to enter the first number.

# 2. Read the input and convert it to an integer.

# 3. Prompt the user to enter the second number.

# 4. Read the input and convert it to an integer.

# 5. Calculate the sum of the two numbers.

# 6. Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

def main():
    print("This program adds two numbers")
    num1: int = int(input("Enter your first number: "))
    num2: int = int(input("Enter your first number: "))
    total_num = num1 + num2
    print(f"The total number is: {total_num}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()