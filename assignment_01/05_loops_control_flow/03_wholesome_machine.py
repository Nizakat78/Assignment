sentence : str = "I am capable of doing anything I put my mind to."


def main():
    print("Please type the following affirmation: " + sentence)

    user_input = input()
    while user_input != sentence:
        print("That was not the affirmation.")
        print("Please type the followin affimation:" + sentence)
        user_input= input()
    print("That's right!")

main()