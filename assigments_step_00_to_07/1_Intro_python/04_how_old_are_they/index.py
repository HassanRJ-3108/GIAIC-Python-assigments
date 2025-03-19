def main():
    # This is a simple program that calculates the ages of 5 people.
    anton: int = 21 # Anton is 21 years old.
    beth:int = 6 + anton # Beth is 6 years younger than Anton.
    chen: int = 20 + beth # Chen is 20 years older than Beth.
    drew: int = chen + anton # Drew is the sum of Chen and Anton's ages.
    ethen: int = chen # Ethen is the same age as Chen.
    
    print(f"Anton's age is: {anton}")
    print(f"Beth's age is: {beth}")
    print(f"Chen's age is: {chen}")
    print(f"Drew's age is: {drew}")
    print(f"Ethen's age is: {ethen}")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()