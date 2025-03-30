import random


word_list = ['python', 'javascript', 'java', 'ruby', 'hangman', 'computer', 'programming', 'development']

def get_random_word():
    """Returns a random word from the list"""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for the unguessed ones"""
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    
    
    word = get_random_word()
    guessed_letters = []
    attempts = 6 
    guessed_word = ['_'] * len(word)  

    print("The word has", len(word), "letters.")
    
  
    while attempts > 0:
        
        print("\nCurrent word:", display_word(word, guessed_letters))
        
        
        guess = input(f"Guess a letter (you have {attempts} attempts left): ").lower()
        
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
       
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.")
            continue

        
        guessed_letters.append(guess)

        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1 
            print(f"Sorry, '{guess}' is not in the word.")

        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

    
    if attempts == 0:
        print(f"\nGame Over! You ran out of attempts. The word was '{word}'.")


if __name__ == "__main__":
    hangman()
