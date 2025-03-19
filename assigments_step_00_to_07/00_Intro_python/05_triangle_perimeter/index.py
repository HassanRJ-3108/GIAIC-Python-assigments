def main():
    # This program calculates the diameter of a triangle
    print("Triangle diameter calculator")
    # Get the sides of the triangle
    side_1: float = float(input("Enter triangle side 1: ")) 
    side_2: float = float(input("Enter triangle side 2: ")) 
    side_3: float = float(input("Enter triangle side 3: "))     
    # Calculate the diameter
    diameter = side_1 + side_2 + side_3
    # Print the diameter
    print("The diameter of a triangle is: ", str(diameter))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()