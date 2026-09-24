def calculate_score(food, max_calories, min_protein, max_budget, mode):
    score = 0

    
    if food["calories"] <= max_calories:
        score += 20

    if food["protein"] >= min_protein:
        score += 20

    if food["price"] <= max_budget:
        score += 20

    
    if food["calories"] <= max_calories:
        calorie_ratio = food["calories"] / max_calories
        score += int((1 - calorie_ratio) * 15)

    
    if food["protein"] >= min_protein:
        protein_ratio = food["protein"] / min_protein

        if protein_ratio >= 2:
            score += 15
        else:
            score += int((protein_ratio - 1) * 15)

    
    if food["price"] <= max_budget:
        budget_ratio = food["price"] / max_budget
        score += int((1 - budget_ratio) * 10)

   
    if mode == "1":  
        if food["calories"] <= max_calories:
            score += 5

    elif mode == "2":  
        if food["protein"] >= min_protein:
            score += 10

    elif mode == "3":  
        if food["calories"] <= max_calories:
            score += 10

    elif mode == "4":  
        if food["price"] <= max_budget:
            score += 10

    return score


def rank_foods(foods, max_calories, min_protein, max_budget, mode):
    ranked_foods = []

    for food in foods:
        score = calculate_score(
            food,
            max_calories,
            min_protein,
            max_budget,
            mode
        )

        ranked_foods.append((score, food))

    ranked_foods.sort(
        reverse=True,
        key=lambda item: item[0]
    )

    return ranked_foods


def find_closest_foods(foods, max_calories, min_protein, max_budget):
    alternatives = []

    for food in foods:
        difference = 0

        if food["calories"] > max_calories:
            difference += food["calories"] - max_calories

        if food["protein"] < min_protein:
            difference += min_protein - food["protein"]

        if food["price"] > max_budget:
            difference += food["price"] - max_budget

        alternatives.append((difference, food))

    alternatives.sort(
        key=lambda item: item[0]
    )

    return alternatives[:3]