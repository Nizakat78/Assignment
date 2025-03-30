def main():
    user_value = int(input("Enter the number: "))  

    while user_value < 100:  
        double_value = user_value * 2  
        
        print(f"Current value: {user_value}")  
        print(f"Doubled value: {double_value}")  

        user_value = double_value  
main()
