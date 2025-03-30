import math

def pythagorean_theorem():
    ab :float =float(input("Enter the length of side AB:"))
    ac :float =float(input("Enter the length of side AC:"))
    bc :float = math.sqrt(ab ** 2 + ac ** 2)
    print(f"The length of side BC is {bc}")

pythagorean_theorem()