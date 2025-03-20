def add_manu_nums():
    """This function takes a list of numbers and returns the sum of those numbers.

    Returns:
        total_num: returns the sum of list of numbers
    """
    num_list: list[int] = [2,4,2,4,6]
    
    total_num = 0
    for i in num_list:
        total_num += i
    return total_num

def main():
    total_num = add_manu_nums()
    print(f"Sum of the list of numbers are: {total_num}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()