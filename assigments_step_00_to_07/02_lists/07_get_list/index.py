def get_list():
    element = input("Enter a value: ")
    my_list = []
    while element != "":
        my_list.append(element)
        element = input("Enter a value: ")
    return my_list

def main():
    my_list = get_list()
    print("Here is the list:", my_list)
    
if __name__ == '__main__':
    main()