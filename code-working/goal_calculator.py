def calculate_debt_repayment(initial_debt, annual_interest_rate, monthly_payment):
    """
    Calculates how long it will take to pay off a debt with fixed monthly payments and
    provides a month-by-month breakdown of interest paid, principal paid, and remaining balance.

    Args:
    initial_debt (float): The initial amount of the debt.
    annual_interest_rate (float): The annual interest rate as a percentage.
    monthly_payment (float): The fixed monthly payment amount.

    Returns:
    None
    """
   
    # Convert annual interest rate to a monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    remaining_balance = initial_debt
    total_interest_paid = 0
    months = 0
   
    print("\nMonth-by-Month Breakdown:")
    print(f"{'Month':<6}{'Interest Paid':<20}{'Principal Paid':<20}{'Remaining Balance'}")
   
    while remaining_balance > 0:
        # Calculate the interest for this month
        interest_paid = remaining_balance * monthly_interest_rate
        # Calculate how much of the payment is applied to the principal
        principal_paid = monthly_payment - interest_paid
       
        if principal_paid <= 0:
            print("Error: Monthly payment is too low to cover interest. Debt cannot be paid off.")
            return
       
        # Update the remaining balance
        remaining_balance -= principal_paid
        # Accumulate the total interest paid
        total_interest_paid += interest_paid
        months += 1
       
        # Print the monthly summary
        print(f"{months:<6}{interest_paid:<20.2f}{principal_paid:<20.2f}{max(remaining_balance, 0):.2f}")
   
    # Final summary
    print(f"\nTotal Interest Paid: ${total_interest_paid:.2f}")
    print(f"Number of Months to Pay Off Debt: {months} months")

# Example usage
initial_debt = float(input("Enter the initial debt amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
monthly_payment = float(input("Enter the fixed monthly payment amount: "))

calculate_debt_repayment(initial_debt, annual_interest_rate, monthly_payment)