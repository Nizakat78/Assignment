def main ():
    user_input: str = input("Please enter an element of the list or press enter to stop.")
    lst: list = []
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop.")
      
    print(lst[len(lst) - 1])
    return(user_input)

main()