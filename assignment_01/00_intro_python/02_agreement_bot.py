user_input = input("What's your favorite animal? ")
formatted_input = f"\033[1;3m {user_input} \033[0m"  # Bold (1) and Italic (3)
print("My favorite animal is also" + formatted_input)
