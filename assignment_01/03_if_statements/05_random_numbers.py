import random


ten_time: int =10
number_1 :int =1
number_2 : int = 100

print("Here is ten differnet numbers:")  
for i in  range(ten_time):
 
    print(random.randint(number_1, number_2), end =" ")
