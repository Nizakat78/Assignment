import random

number_of_dices = 6

def roll_dice(labal):
    dice_roll_1: int = random.randint(1, number_of_dices)
    dice_roll_2: int = random.randint(1, number_of_dices)
    total: int = dice_roll_1 + dice_roll_2

    print(f"{labal} {total}")

roll_dice("first two dices rolled:") 
roll_dice("second two dices rolled:")
roll_dice("third two dices rolled:")






