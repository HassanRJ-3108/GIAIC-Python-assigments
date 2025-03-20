def main():
    message: str = input("Enter a message to copy: ")
    message_list: list[str] = []
    print("list before:", message_list)
    message_list.append(message)
    message_list.append(message)
    message_list.append(message)
    print("List after:", message_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()