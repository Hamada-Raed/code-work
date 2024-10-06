def calculate_min_bills(bills, amount):
    # Sort bills in descending order to prioritize larger denominations
    bills.sort(reverse=True)
   
    result = {}
    remaining_amount = amount
   
    for bill in bills:
        if remaining_amount >= bill:
            count = remaining_amount // bill  # Determine how many bills of this denomination
            result[bill] = count  # Store the count for the current denomination
            remaining_amount -= bill * count  # Subtract the amount covered by these bills

    if remaining_amount > 0:
        return "Unable to withdraw the exact amount with available denominations."
   
    return result

# Example usage:
bills = [100, 50, 20, 10, 5, 1]  # Available bill denominations
amount = 276  # Amount to withdraw

min_bills = calculate_min_bills(bills, amount)
print(min_bills)