def main():
     list=[]
    
     value = input("Eneter the Value")
    while value :
        list.append(value)
        value = input('Enter the Value')
        print("Here is List:", list)

main()