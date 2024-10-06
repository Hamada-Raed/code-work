import datetime

# Function to add food and its nutritional values
def add_food(log, food, calories, proteins, carbs, fats):
    log.append({
        'date': datetime.date.today(),
        'food': food,
        'calories': calories,
        'proteins': proteins,
        'carbs': carbs,
        'fats': fats
    })

# Function to calculate total intake
def calculate_totals(log):
    totals = {'calories': 0, 'proteins': 0, 'carbs': 0, 'fats': 0}
    for entry in log:
        totals['calories'] += entry['calories']
        totals['proteins'] += entry['proteins']
        totals['carbs'] += entry['carbs']
        totals['fats'] += entry['fats']
    return totals

# Function to display log and totals
def display_log(log):
    for entry in log:
        print(f"Date: {entry['date']}, Food: {entry['food']}, Calories: {entry['calories']}, Proteins: {entry['proteins']}g, Carbs: {entry['carbs']}g, Fats: {entry['fats']}g")
    totals = calculate_totals(log)
    print(f"Total Intake - Calories: {totals['calories']}, Proteins: {totals['proteins']}g, Carbs: {totals['carbs']}g, Fats: {totals['fats']}g")

# Example usage
log = []
add_food(log, "Chicken Breast", 165, 31, 0, 3.6)
add_food(log, "Brown Rice", 215, 5, 45, 1.6)
display_log(log)