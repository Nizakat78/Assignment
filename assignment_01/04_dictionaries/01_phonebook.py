def read_number():
    phone_book = {}

    while True:
        Name_input = input("Enter the name: ")
        if Name_input == "":
            break
        phone_number = input("Enter the Number: ")
        phone_book[Name_input] = phone_number
    
    return phone_book  # Move return statement outside of the loop

def print_phone_book(phone_book):
    for Name_input in phone_book:
        print(str(Name_input) + " -> " + str(phone_book[Name_input]))

def look_numbers(phone_book):
    while True:
        Name_input = input("Enter name to lookup: ")
        if Name_input == "":
            break
        if Name_input not in phone_book:
            print(Name_input + " is not in the phonebook")
        else:
            print(phone_book[Name_input])

def main():
    phone_book = read_number()
    print_phone_book(phone_book)
    look_numbers(phone_book)

main()
