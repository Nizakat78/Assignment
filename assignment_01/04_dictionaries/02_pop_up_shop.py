def main():
    fruits_items = {"Apple": 3, "Banana": 2, "Kiwi": 1,  "Orange": 5, "mango": 4, "durian": 2.5, "grapes": 3.5}

    total_cost_fruit = 0
    for fruits_collect in fruits_items:
        price = fruits_items[fruits_collect]
        amount_bought = int(input("How many (" + fruits_collect + ") do you want to buy?"))
        total_cost_fruit += (price * amount_bought)
    print("Your total is $" + str(total_cost_fruit))


main()