def main():
    
    C = 299792458 # Speed of light in m/s
    M: float = float(input("Enter mass in kilograms: ")) # Taking mass as input from user in kilograms
    E: float = M * C ** 2 # Calculating energy using formula E = MC^2
    print(f"Energy = {E} Joules") # Displaying the energy in Joules

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

