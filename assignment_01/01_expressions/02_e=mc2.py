C = 299792458

def  main():
    mass_in_kg :float =float(input("Enter mass in kg:"))

    energy_in_joules :float = mass_in_kg * C ** 2
    print(mass_in_kg)
    print("m*C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"{C} = speed of light in m/s")
    print(f"{energy_in_joules} joules of energy!")

main()