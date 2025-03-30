user_input: int =int(input("Enter the years "))

if user_input % 4 == 0:
    if user_input % 100 == 0:
        if user_input % 400 == 0:
            print("The year is a leap year!")
        else:
             print("The year is not a leap year")
    else:
         print("That's a leap year!")
else:
     print("The year is not a leap year")


  