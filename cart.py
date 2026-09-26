def add_to_cart(cart, food, quantity):
    for item in cart:
        if item["food"]["name"].lower() == food["name"].lower():
            item["quantity"] += quantity
            print(
                food["name"],
                "quantity updated to",
                item["quantity"]
            )
            return

    cart.append({"food": food,"quantity": quantity})

    print(food["name"],"x",quantity, "added to cart.")


def remove_from_cart(cart, item_number, quantity):
    if item_number < 1 or item_number > len(cart):
        print("Invalid cart item number.")
        return

    item = cart[item_number - 1]
    food = item["food"]

    if quantity > item["quantity"]:
        print("You only have", item["quantity"], food["name"], "in your cart.")
        return

    item["quantity"] -= quantity

    if item["quantity"] == 0:
        cart.pop(item_number - 1)
        print(food["name"], "removed from cart.")

    else:
        print(quantity, food["name"], "removed.")
        print("Remaining:",food["name"],"| Qty:",item["quantity"])


def view_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    total_price = 0
    total_calories = 0
    total_protein = 0

    for number, item in enumerate(cart, start=1):

        food = item["food"]
        quantity = item["quantity"]

        item_price = food["price"] * quantity
        item_calories = food["calories"] * quantity
        item_protein = food["protein"] * quantity

        print(number,".",food["name"],"| Qty:", quantity,"| ₹",item_price)

        total_price += item_price
        total_calories += item_calories
        total_protein += item_protein

    print("-------------------------------")
    print("Total Price: ₹", total_price)
    print("Total Calories:", total_calories)
    print("Total Protein:", total_protein, "g")


def checkout(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    total_price = 0
    total_calories = 0
    total_protein = 0

    print("\n========== CHECKOUT ==========")

    for item in cart:

        food = item["food"]
        quantity = item["quantity"]

        item_price = food["price"] * quantity
        item_calories = food["calories"] * quantity
        item_protein = food["protein"] * quantity

        print(food["name"],"| Qty:",quantity,"| ₹",item_price)

        total_price += item_price
        total_calories += item_calories
        total_protein += item_protein

    print("-------------------------------")
    print("Total Price: ₹", total_price)
    print("Total Calories:", total_calories)
    print("Total Protein:", total_protein, "g")

    print("\nPayment Method")
    print("1. UPI")
    print("2. Card")
    print("3. Cash on Delivery")

    payment = input("Choose payment method: ").strip()

    if payment == "1":
        print("\nUPI payment selected.")
        print("Payment successful.")

    elif payment == "2":
        print("\nCard payment selected.")
        print("Payment successful.")

    elif payment == "3":
        print("\nCash on Delivery selected.")
        print("Order will be paid on delivery.")

    else:
        print("Invalid payment method.")
        return

    print("\n========== ORDER CONFIRMED ==========")
    print("Thank you for ordering from SmartBite!")
    print("Total Amount: ₹", total_price)
    print("=====================================")

    cart.clear()