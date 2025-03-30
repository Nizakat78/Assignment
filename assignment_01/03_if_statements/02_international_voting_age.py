Peturksbouipo: int =16

Stanlau: int = 25

Mayengua: int =48

def main():
    user_input :int= int(input(" How old are you? "))
    if user_input >= Peturksbouipo:
        print("You can vote in Peturksbouipo where the voting age is " + str(Peturksbouipo) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(Peturksbouipo) + ".")
    
    if user_input >= Stanlau:
        print("You can vote in Peturksbouipo where the voting age is " + str(Stanlau) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(Stanlau) + ".")
    if user_input >= Mayengua:
        print("You can vote in Peturksbouipo where the voting age is " + str(Mayengua) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(Mayengua) + ".")


main()