import math
def main():
    """This function calculates the hypotenuse of a right triangle given the values of the other two sides.
    """
    AB: float = float(input("Enter a value for side AB: "))
    AC: float = float(input("Enter a value for side AC: "))
    
    AB_AC = math.sqrt(AB**2 + AC**2)
    print("The hypotenuse of the triangle is: ", AB_AC)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()