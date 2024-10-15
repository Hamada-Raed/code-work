def calculate_intake(food_items):
    """
    Calculate the total protein and calorie intake based on a list of food items.
    
    Each food item should be a dictionary with keys 'name', 'protein', and 'calories'.
    
    Args:
        food_items (list of dict): A list of food items with their respective protein and calorie content.

    Returns:
        tuple: Total protein intake in grams and total calorie intake in kcal.
    """
    total_protein = 0
    total_calories = 0
    
    for item in food_items:
        total_protein += item.get('protein', 0)
        total_calories += item.get('calories', 0)
    
    return total_protein, total_calories


food_items = [
    {'name': 'Steak', 'protein': 42, 'calories': 679},
    {'name': 'Mashed Potatoes', 'protein': 4, 'calories': 214},
    {'name': 'Cheese', 'protein': 7, 'calories': 113}
]
def calculate_intake(food_items):
    """
    Calculate the total protein and calorie intake based on a list of food items.
    
    Each food item should be a dictionary with keys 'name', 'protein', and 'calories'.
    
    Args:
        food_items (list of dict): A list of food items with their respective protein and calorie content.

    Returns:
        tuple: Total protein intake in grams and total calorie intake in kcal.
    """
    total_protein = 0
    total_calories = 0
    
    for item in food_items:
        # Check if the item is a dictionary
        if not isinstance(item, dict):
            print(f"Warning: {item} is not a dictionary and will be skipped.")
            continue

        # Safely retrieve protein and calories, defaulting to 0
        protein = item.get('protein', 0)
        calories = item.get('calories', 0)

        # Ensure protein and calories are numeric values
        if not isinstance(protein, (int, float)) or not isinstance(calories, (int, float)):
            print(f"Warning: Protein or calories for {item['name']} are not numeric and will be set to 0.")
            protein = 0
            calories = 0
        
        total_protein += protein
        total_calories += calories
    
    return total_protein, total_calories

# Test Case 1: Basic Intake
food_items1 = [
    {'name': 'Chicken Breast', 'protein': 31, 'calories': 165},
    {'name': 'Rice', 'protein': 4, 'calories': 130},
    {'name': 'Broccoli', 'protein': 3, 'calories': 55}
]
total_protein1, total_calories1 = calculate_intake(food_items1)
print(f"Test Case 1: Basic Intake - Total Protein: {total_protein1}g, Total Calories: {total_calories1}kcal")
# Expected Output: (38, 350)

# Test Case 2: High-Calorie Meal
food_items2 = [
    {'name': 'Steak', 'protein': 42, 'calories': 679},
    {'name': 'Mashed Potatoes', 'protein': 4, 'calories': 214},
    {'name': 'Cheese', 'protein': 7, 'calories': 113}
]
total_protein2, total_calories2 = calculate_intake(food_items2)
print(f"Test Case 2: High-Calorie Meal - Total Protein: {total_protein2}g, Total Calories: {total_calories2}kcal")
# Expected Output: (53, 1006)

# Test Case 3: Empty Food List
food_items3 = []
total_protein3, total_calories3 = calculate_intake(food_items3)
print(f"Test Case 3: Empty Food List - Total Protein: {total_protein3}g, Total Calories: {total_calories3}kcal")
# Expected Output: (0, 0)

# Test Case 4: Food Item Without Protein or Calories
food_items4 = [
    {'name': 'Apple', 'calories': 95},
    {'name': 'Banana', 'protein': 1}
]
total_protein4, total_calories4 = calculate_intake(food_items4)
print(f"Test Case 4: Food Item Without Protein or Calories - Total Protein: {total_protein4}g, Total Calories: {total_calories4}kcal")
# Expected Output: (1, 95)

# Test Case 5: Non-Dictionary Food Item
food_items5 = [
    {'name': 'Chicken Breast', 'protein': 31, 'calories': 165},
    'Non-dictionary item',
    {'name': 'Broccoli', 'protein': 3, 'calories': 55}
]
total_protein5, total_calories5 = calculate_intake(food_items5)
print(f"Test Case 5: Non-Dictionary Food Item - Total Protein: {total_protein5}g, Total Calories: {total_calories5}kcal")
# Expected Output: (34, 220)

# Test Case 6: Food Item with Non-Numeric Protein or Calories
food_items6 = [
    {'name': 'Chicken Breast', 'protein': 'thirty-one', 'calories': 165},
    {'name': 'Rice', 'protein': 4, 'calories': 'one hundred thirty'}
]
total_protein6, total_calories6 = calculate_intake(food_items6)
print(f"Test Case 6: Food Item with Non-Numeric Protein or Calories - Total Protein: {total_protein6}g, Total Calories: {total_calories6}kcal")
# Expected Output: (4, 165)
