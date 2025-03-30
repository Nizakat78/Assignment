

def remainder_check():
    dividend : int =int(input("Please enter an integer to be divided:"))
    divisor :int =int(input("Please enter an integer to divide by:"))
    remainder :int = dividend % divisor
    quotient :int = dividend // divisor
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

remainder_check()