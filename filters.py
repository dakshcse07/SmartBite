def filter_foods(foods, max_calories, min_protein, max_budget,
                 brand="All", category="All"):

    results = []

    brand = brand.strip().lower()
    category = category.strip().lower()

    for food in foods:

        if (
            food["calories"] <= max_calories
            and food["protein"] >= min_protein
            and food["price"] <= max_budget
        ):

            food_brand = food["brand"].strip().lower()
            food_category = food["category"].strip().lower()

            if brand != "all" and food_brand != brand:
                continue

            if category != "all" and food_category != category:
                continue

            results.append(food)

    return results