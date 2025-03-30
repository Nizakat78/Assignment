min_height : float = 40

user_input :float =float(input("How tall are you? "))

if user_input >= min_height:
    print("You're tall enough to ride!")
else:
     print("You're not tall enough to ride, but maybe next year!")