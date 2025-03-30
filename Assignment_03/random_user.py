def main():
    print("Welcome to the 'Guess the Number' game!")
    print("Pick a number between 1 and 100, and I will try to guess it!")
    print("Please respond with 'too high', 'too low', or 'correct'.")

    low = 1
    high = 100
    attempts = 0

    while True:
        
        guess = (low + high) // 2
        attempts += 1

        
        print(f"Is your number {guess}?")
        user_response = input("Enter 'too high', 'too low', or 'correct': ").lower()

        
        if user_response == "too high":
            high = guess - 1  
        elif user_response == "too low":
            low = guess + 1  
        elif user_response == "correct":
            print(f"Yay! I guessed your number {guess} correctly in {attempts} attempts!")
            break  
        else:
            print("Invalid response. Please respond with 'too high', 'too low', or 'correct'.")

if __name__ == "__main__":
    main()
