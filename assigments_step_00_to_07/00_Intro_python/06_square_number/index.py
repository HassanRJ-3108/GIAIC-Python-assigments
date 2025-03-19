def main():
    """This function asks the user for a number and prints the square of that number.
    """
    # Ask the user for a number
    num: float = float(input("Type a number to see its square: ") ) 
    # Print the square of the number
    print(f"The square of {num} is {num**2}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
