def main():
    print("Welcome to the Mad Libs Game!")
    
    # Collect inputs from the user for different parts of speech
    adjective = input("Enter an adjective: ")
    noun1 = input("Enter a noun (singular): ")
    noun2 = input("Enter another noun (singular): ")
    verb1 = input("Enter a verb (past tense): ")
    verb2 = input("Enter another verb (past tense): ")
    number = input("Enter a number: ")
    
   
    story = f"One day, a very {adjective} {noun1} was walking down the street. It saw a {noun2} and {verb1} right past it. The {noun1} continued to {verb2} for {number} miles and then took a nap."
    
   
    print("\nHere is your Mad Lib story:")
    print(story)


main()
