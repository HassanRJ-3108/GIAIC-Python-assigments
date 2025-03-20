def main():
    """This program convert feet to inches.
    """
    inches_in_foot = 12 # 1 foot = 12 inches
    feet: float = float(input("Enter the feet: ")) # get feet from user
    feet = feet * inches_in_foot # convert feet to inches
    print("That is", feet, "inches.") # print the result


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()