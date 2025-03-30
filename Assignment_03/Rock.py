import random

def get_computer_choice():
    """Returns a random choice for the computer: rock, paper, or scissors."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determines the winner between the user and the computer."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'exit' to quit): ").lower()

        if user_choice == "exit":
            print("Thanks for playing!")
            break

        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        
        computer_choice = get_computer_choice()
        print(f"The computer chose {computer_choice}.")

       
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
