import random

def main():
    print("We are playing a Game")

    secret_number = random.randint(1, 99) 

    print("I am thinking of a number between 1 and 99... ")

    while True:  
        try:
            choose_number = int(input("Enter your guess: "))  
            if choose_number < secret_number:
                print("Your guess is too low")
            elif choose_number > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  
        except ValueError:  
            print("Please enter a valid number.")

main()
