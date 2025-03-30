def  add_three_times(my_list, data):
    for i in range(3):
        my_list.append(data)



def main():
    message =input('Enter a message:')
    my_list = []
    print("Before List:",my_list)
    add_three_times(my_list, message)
    print("After List", my_list)

main()