def get_last_element(lst):
    print(lst[-1])
    
def get_list_from_user():
    my_list: list = []
    element: str = input("Enter element or press enter to process: ")
    while element != "":
        my_list.append(element)
        element: str = input("Enter element or press enter to process: ")
        
    return my_list

def main():
    my_list = get_list_from_user()
    get_last_element(my_list)
    
if __name__ == '__main__':
    main()