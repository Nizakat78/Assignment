import random

def main():
    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 100)

    
    attempts = 0

    while True:
        try:
            
            guess = int(input("Enter your guess: "))
            attempts += 1  

            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congrats! You guessed the number {secret_number} correctly in {attempts} attempts.")
                break  
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
