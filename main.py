from food_data import FOODS
from validation import get_positive_number
from filters import filter_foods
from recommender import rank_foods, find_closest_foods
from comparison import compare_foods
from cart import add_to_cart, remove_from_cart, view_cart, checkout
from user import register_user, login_user, guest_user


cart = []


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_food_from_result(item):
    if isinstance(item, tuple):
        return item[1]

    return item


def show_order_list(cart):

    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== ORDER LIST ==========")

    total_amount = 0

    for number, item in enumerate(cart, start=1):

        food = item["food"]
        quantity = item["quantity"]

        item_total = food["price"] * quantity

        total_amount += item_total

        print(
            number,
            ".",
            food["name"],
            "|",
            food["brand"],
            "| Qty:",
            quantity,
            "| ₹",
            item_total
        )

    print("-------------------------------")
    print("Total Amount: ₹", total_amount)

    print("\nThank you for adding items to your cart!")


def add_multiple_foods(food_list):

    if not food_list:
        print("No foods available.")
        return

    while True:

        print("\n========== SELECT FOOD ==========")

        for number, item in enumerate(food_list, start=1):

            food = get_food_from_result(item)

            print(
                number,
                ".",
                food["name"],
                "|",
                food["brand"],
                "|",
                food["category"],
                "| ₹",
                food["price"]
            )

        print("0. Finish adding")

        choice = input("Enter food number to add: ").strip()

        if choice == "0":
            break

        try:

            number = int(choice)

            if number < 1 or number > len(food_list):
                print("Invalid food number.")
                continue

            selected_food = get_food_from_result(
                food_list[number - 1]
            )

            quantity = get_quantity()

            add_to_cart(cart,selected_food,quantity)

        except ValueError:

            print("Please enter a valid number.")

    if cart:
        show_order_list(cart)


def recommendation_flow():

    print("\n========== FOOD RECOMMENDATIONS ==========")

    print("\nSelect Mode")
    print("1. Cheat Meal")
    print("2. High Protein")
    print("3. Low Calorie")
    print("4. Best Value")

    mode = input("Choose mode: ").strip()

    if mode not in ["1", "2", "3", "4"]:
        print("Invalid mode.")
        return

    print("\nSelected Mode:", mode)

    max_calories = get_positive_number(
        "Enter maximum calories: "
    )

    min_protein = get_positive_number(
        "Enter minimum protein (g): "
    )

    max_budget = get_positive_number(
        "Enter maximum budget (₹): "
    )
    print("\n========== BRAND ==========")

    brands = sorted(
        set(food["brand"] for food in FOODS)
    )

    print("0. All")

    for number, brand_name in enumerate(brands, start=1):
        print(number, ".", brand_name)

    brand_choice = input("Choose brand: ").strip()

    if brand_choice == "0":

        brand = "All"

    else:

        try:

            brand_number = int(brand_choice)

            if 1 <= brand_number <= len(brands):
                brand = brands[brand_number - 1]

            else:
                print("Invalid brand.")
                return

        except ValueError:

            print("Invalid brand.")
            return

    

    print("\n========== CATEGORY ==========")

    categories = sorted(
        set(food["category"] for food in FOODS)
    )

    print("0. All")

    for number, category_name in enumerate(categories, start=1):
        print(number, ".", category_name)

    category_choice = input("Choose category: ").strip()

    if category_choice == "0":

        category = "All"

    else:

        try:

            category_number = int(category_choice)

            if 1 <= category_number <= len(categories):
                category = categories[category_number - 1]

            else:
                print("Invalid category.")
                return

        except ValueError:

            print("Invalid category.")
            return

    

    results = filter_foods(
        FOODS,
        max_calories,
        min_protein,
        max_budget,
        brand,
        category
    )

    

    if results:

        ranked_results = rank_foods(
            results,
            max_calories,
            min_protein,
            max_budget,
            mode
        )

        print("\n========== RECOMMENDED FOODS ==========")

        for number, item in enumerate(
            ranked_results,
            start=1
        ):

            
            score = item[0]
            food = item[1]

            print(
                number,
                ".",
                food["name"],
                "|",
                food["brand"],
                "|",
                food["calories"],
                "calories |",
                food["protein"],
                "g protein | ₹",
                food["price"],
                "| Score:",
                score
            )

        while True:

            print("\n---------- ACTIONS ----------")
            print("1. Compare foods")
            print("2. Add food to cart")
            print("3. View cart")
            print("4. Search again")
            print("5. Main menu")

            action = input("Choose an option: ").strip()

            if action == "1":
                recommended_foods = [
                    item[1] for item in ranked_results
                    ]
                compare_foods(recommended_foods)

            elif action == "2":

                add_multiple_foods(
                    ranked_results
                )

            elif action == "3":

                view_cart(cart)

            elif action == "4":

                return

            elif action == "5":

                return

            else:

                print("Invalid option.")

   
    else:

        print("\nNo exact matches found.")

        closest = find_closest_foods(
            FOODS,
            max_calories,
            min_protein,
            max_budget
        )

        if not closest:

            print("No suitable alternatives found.")
            return

        print(
            "\n========== CLOSEST ALTERNATIVES =========="
        )

        for number, item in enumerate(
            closest,
            start=1
        ):

            

            food = item[1]

            print(
                number,
                ".",
                food["name"],
                "|",
                food["brand"],
                "|",
                food["calories"],
                "calories |",
                food["protein"],
                "g protein | ₹",
                food["price"]
            )

        while True:

            print("\n---------- ACTIONS ----------")
            print("1. Add food to cart")
            print("2. Search again")
            print("3. Main menu")

            action = input("Choose an option: ").strip()

            if action == "1":

                add_multiple_foods(
                    closest
                )

            elif action == "2":

                return

            elif action == "3":

                return

            else:

                print("Invalid option.")


def remove_food_from_cart():

    if not cart:

        print("\nYour cart is empty.")
        return

    view_cart(cart)

    print("\n========== REMOVE FROM CART ==========")

    try:

        item_number = int(
            input(
                "Enter cart item number to remove: "
            ).strip()
        )

    except ValueError:

        print("Please enter a valid number.")
        return

    if item_number < 1 or item_number > len(cart):

        print("Invalid cart item number.")
        return

    available_quantity = cart[
        item_number - 1
    ]["quantity"]

    print(
        "Available quantity:",
        available_quantity
    )

    quantity = get_quantity()

    remove_from_cart(
        cart,
        item_number,
        quantity
    )


def main_menu():

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Find food recommendations")
        print("2. View cart")
        print("3. Remove food from cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            recommendation_flow()

        elif choice == "2":

            view_cart(cart)

        elif choice == "3":

            remove_food_from_cart()

        elif choice == "4":

            checkout(cart)

        elif choice == "5":

            print(
                "\nThank you for using SmartBite!"
            )
            break

        else:

            print("Invalid option.")


def start_program():

    print("\n====================================")
    print("        WELCOME TO SMARTBITE")
    print("====================================")

    while True:

        print("\n1. Login")
        print("2. Register")
        print("3. Continue as Guest")
        print("4. Exit")

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            user = login_user()

            if user:
                main_menu()

                break

        elif choice == "2":

            register_user()

        elif choice == "3":

            guest_user()

            main_menu()

            break

        elif choice == "4":

            print(
                "\nThank you for using SmartBite!"
            )
            break

        else:

            print("Invalid option.")


start_program()