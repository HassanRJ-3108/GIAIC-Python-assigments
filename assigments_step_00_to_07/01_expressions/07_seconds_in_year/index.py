SECONDS_IN_MINUTE: int = 60
MINUTES_INT_HOUR: int = SECONDS_IN_MINUTE * 60
HOURS_IN_DAY: int = MINUTES_INT_HOUR * 24
DAYS_IN_YEAR: int = HOURS_IN_DAY * 365



def main():
    user_input_in_year: int = int(input("Enter number of years to convert in seconds: "))
    total_seconds_in_year: int = user_input_in_year * DAYS_IN_YEAR
    print(f"The total number of seconds in {user_input_in_year} are: {total_seconds_in_year}")
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()