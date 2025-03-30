import random

number_of_dices = 6

def roll_dice():
    dice_1 :int= random.randint(1, number_of_dices)
    dice_2:int =random.randint(1, number_of_dices)
    total_dice :int =dice_1 +dice_2

    print(f"Dice have {number_of_dices} sides each")
    print("First dice rolled:",dice_1)
    print("Second dice rolled:",dice_2)
    print(f"Total is {total_dice}")

roll_dice()