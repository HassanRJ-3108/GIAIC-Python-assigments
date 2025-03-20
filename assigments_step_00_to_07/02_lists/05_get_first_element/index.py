def get_first_element(lst):
    print(lst[0])
    
def get_list_by_user():
    element: str = input("Please enter an element of the list or press enter to stop: ")
    my_list: list = []
    while element != "":
        my_list.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return my_list

def main():
    my_list = get_list_by_user()
    get_first_element(my_list)
    
if __name__ == '__main__':
    main()