# Define a function to add a chemical to the inventory
def add_chemical(inventory, name, quantity, concentration):
    if name in inventory:
        # Update the existing chemical's quantity
        inventory[name]['quantity'] += quantity
    else:
        # Add a new chemical to the inventory
        inventory[name] = {'quantity': quantity, 'concentration': concentration}
    return inventory

# Define a function to remove a chemical from the inventory
def remove_chemical(inventory, name, quantity):
    if name not in inventory:
        print(f"Error: {name} not found in inventory.")
        return inventory

    if inventory[name]['quantity'] < quantity:
        print(f"Error: Cannot remove {quantity} liters of {name}. Only {inventory[name]['quantity']} liters available.")
        return inventory

    # Subtract the specified quantity
    inventory[name]['quantity'] -= quantity

    # Remove the chemical if its quantity reaches zero
    if inventory[name]['quantity'] == 0:
        del inventory[name]

    return inventory

# Example usage of the chemical inventory system
def main():
    # Initialize an empty inventory
    inventory = {}

    # Add chemicals to the inventory
    inventory = add_chemical(inventory, 'Acetone', 5, 99.5)
    inventory = add_chemical(inventory, 'Ethanol', 10, 95.0)
    inventory = add_chemical(inventory, 'Methanol', 8, 99.9)

    # Display the current inventory
    print("Initial Inventory:", inventory)

    # Remove some chemicals
    inventory = remove_chemical(inventory, 'Acetone', 3)
    inventory = remove_chemical(inventory, 'Ethanol', 10)  # This should remove Ethanol completely
    inventory = remove_chemical(inventory, 'Methanol', 9)  # This should show an error

    # Display the updated inventory
    print("Updated Inventory:", inventory)

if __name__ == "__main__":
    main()