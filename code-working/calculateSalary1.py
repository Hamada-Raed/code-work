def calculate_salary(base_salary, experience_years, rating):
    """
    Calculates the total salary for an employee based on their base salary, experience, and performance rating.

    Args:
        base_salary (float): The base salary of the employee.
        experience_years (int): The number of years the employee has worked.
        rating (float): The employee's performance rating on a scale of 1 to 5.

    Returns:
        float: The total salary for the employee.
    """
    # Apply experience bonus if applicable
    if experience_years > 5:
        total_salary = base_salary * 1.10  # 10% bonus for experience
    else:
        total_salary = base_salary

    # Apply performance bonus if applicable
    if rating >= 4.5:
        total_salary *= 1.15  # 15% performance bonus

    return total_salary


def calculate_bonus(total_salary, performance_rating):
    """
    Calculates an additional bonus for top performers based on their total salary and performance rating.

    Args:
        total_salary (float): The total salary of the employee.
        performance_rating (float): The employee's performance rating.

    Returns:
        float: The additional bonus amount.
    """
    # Determine bonus percentage based on performance rating
    if performance_rating == 5:
        bonus_percentage = 0.20  # 20% bonus for top performers
    elif 4.5 <= performance_rating < 5:
        bonus_percentage = 0.10  # 10% bonus for high performers
    else:
        bonus_percentage = 0  # No additional bonus for others

    # Calculate additional bonus
    additional_bonus = total_salary * bonus_percentage

    return additional_bonus


# Example usage:
base_salary = 50000
experience_years = 10
performance_rating = 4.8

# Step 1: Calculate total salary
total_salary = calculate_salary(base_salary, experience_years, performance_rating)

# Step 2: Calculate additional bonus
additional_bonus = calculate_bonus(total_salary, performance_rating)

# Output the results
print(f"Total Salary: ${total_salary:.2f}")
print(f"Additional Bonus: ${additional_bonus:.2f}")