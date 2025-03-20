def main():
    numbers: list = [1, 2, 3, 4, 5]
    for number in range(len(numbers)):
        numbers[number] = numbers[number] + numbers[number]
    print(numbers)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()