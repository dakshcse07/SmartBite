def compare_foods(foods):

    if len(foods) < 2:
        print("Not enough foods are available for comparison.")
        return

    print("\n========== FOOD COMPARISON ==========")

    print("\nAvailable foods:")

    for number, food in enumerate(foods, start=1):
        print(number,".",food["name"],"-",food["brand"])

    try:
        first = int(input("\nEnter first food number: "))
        second = int(input("Enter second food number: "))

        if first < 1 or first > len(foods):
            print("Invalid first food number.")
            return

        if second < 1 or second > len(foods):
            print("Invalid second food number.")
            return

        if first == second:
            print("Please select two different foods.")
            return

        food1 = foods[first - 1]
        food2 = foods[second - 1]

        print("\n========== COMPARISON ==========")

        print("\nFood:")
        print(food1["name"], "vs", food2["name"])

        print("\nBrand:")
        print(food1["brand"], "vs", food2["brand"])

        print("\nCategory:")
        print(food1["category"], "vs", food2["category"])

        print("\nCalories:")
        print(food1["calories"],"vs",food2["calories"])

        print("\nProtein:")
        print(food1["protein"],"g vs",food2["protein"],"g")

        print("\nPrice:")
        print("₹", food1["price"],"vs ₹", food2["price"])

        print("\n================================")

    except ValueError:
        print("Please enter valid numbers.")