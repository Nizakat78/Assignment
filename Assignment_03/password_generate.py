import random
import string

def generate_password(length):
    """Function to generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_valid_input(prompt):
    """Function to ensure valid numeric input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    # Use the function to get valid input from the user
    num_passwords = get_valid_input("Enter the number of passwords you want to generate: ")
    password_length = get_valid_input("Enter the length of each password: ")

    print("\nGenerated Passwords:")
    
    for _ in range(num_passwords):
        print(generate_password(password_length))

if __name__ == "__main__":
    main()
