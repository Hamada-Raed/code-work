def calculate_salary(base_salary, experience_years, rating):
    """
    Calculate the total salary for an employee based on base salary, experience, and performance rating.

    Parameters:
    - base_salary (float): The base salary of the employee.
    - experience_years (int): The number of years the employee has worked.
    - rating (float): The employee’s performance rating on a scale of 1 to 5.

    Returns:
    - float: The total salary for the employee.
    """
    # Start with the base salary
    total_salary = base_salary

    # Add a 10% bonus if experience is greater than 5 years
    if experience_years > 5:
        total_salary += base_salary * 0.10

    # Add a 15% performance bonus if the rating is 4.5 or higher
    if rating >= 4.5:
        total_salary += total_salary * 0.15

    return total_salary

def calculate_bonus(total_salary, performance_rating):
    """
    Calculate the additional bonus for top performers based on their performance rating.

    Parameters:
    - total_salary (float): The total salary of the employee.
    - performance_rating (float): The employee’s performance rating.

    Returns:
    - float: The additional bonus amount.
    """
    additional_bonus = 0.0

    # Add a 20% bonus if the performance rating is 5
    if performance_rating == 5:
        additional_bonus = total_salary * 0.20
    # Add a 10% bonus if the performance rating is between 4.5 and 4.99
    elif 4.5 <= performance_rating < 5:
        additional_bonus = total_salary * 0.10

    return additional_bonus

# Example usage
base_salary = 50000.0
experience_years = 6
rating = 4.7

# Calculate the total salary
total_salary = calculate_salary(base_salary, experience_years, rating)

# Calculate the additional bonus
additional_bonus = calculate_bonus(total_salary, rating)

# Print the results
print(f"Total Salary: ${total_salary:.2f}")
print(f"Additional Bonus: ${additional_bonus:.2f}")