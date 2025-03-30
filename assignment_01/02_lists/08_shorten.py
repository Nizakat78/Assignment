# MAX_LENGTH = 10  # Define the maximum allowed length of the list

# def shorten(lst):
#     while len(lst) > MAX_LENGTH:
#         last_elem = lst.pop()
#         print(last_elem)

# # There is no need to edit code beyond this point

# def get_lst():
#     """
#     Prompts the user to enter one element of the list at a time and returns the resulting list.
#     """
#     lst = []
#     elem = input("Please enter an element of the list or press enter to stop. ")
#     while elem != "":
#         lst.append(elem)
#         elem = input("Please enter an element of the list or press enter to stop. ")
#     return lst

# def main():
#     lst = get_lst()
#     shorten(lst)


# if __name__ == '__main__':
#     main()




Mix_length = 10


def list_length (list):
    while len(list) > Mix_length:
        last_element = list.pop()
        print(last_element)


def main_list():
    list =[]
    element = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        list.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return list

def main():
    list = main_list()
    list_length(list)


main()