def user_input():
    user_number = []
    while True:
        user_input = input("Please enter a number, or a blank line to finish: ")
        if user_input == "":
            break
        try:
            convert_number = int(user_input)  # Convert input to integer
            user_number.append(convert_number)  # Append the number to the list
        except ValueError:
            print("Please enter a valid number.")  # If the input is not a valid number, ask again
    return user_number

def dict_add(number_add_list):
    empty_dict = {}  # Rename the dictionary to a more readable name
    for number in number_add_list:
        if number not in empty_dict:
            empty_dict[number] = 1  # If the number is not in the dictionary, add it with count 1
        else:
            empty_dict[number] += 1  # If the number is already in the dictionary, increment its count
    return empty_dict

def number_show(empty_dict):
    for number in empty_dict:
        print(f"{number} appears {empty_dict[number]} times.")  # Use f-strings for easier formatting

def main():
    user_number = user_input()  # Get the user's numbers
    empty_dict = dict_add(user_number)  # Count the occurrences of each number
    number_show(empty_dict)  # Display the results

main()
