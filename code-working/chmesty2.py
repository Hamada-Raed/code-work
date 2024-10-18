class ChemicalInventory:
    def __init__(self):
        # Initialize an empty inventory
        self.inventory = {}

    def add_chemical(self, name, quantity, concentration):
        # Check if the chemical already exists in the inventory
        if name in self.inventory:
            print(f"Chemical '{name}' already exists in the inventory.")
            return
        # Add the chemical to the inventory
        self.inventory[name] = {"quantity": quantity, "concentration": concentration}

    def remove_chemical(self, name, quantity):
        # Check if the chemical exists in the inventory
        if name not in self.inventory:
            print(f"Chemical '{name}' does not exist in the inventory.")
            return self.inventory
        # Check if the quantity to remove is greater than the available quantity
        if quantity > self.inventory[name]["quantity"]:
            print(f"Error: Cannot remove {quantity} liters of '{name}' as only {self.inventory[name]['quantity']} liters are available.")
            return self.inventory
        # Update the quantity of the chemical
        self.inventory[name]["quantity"] -= quantity
        # If the quantity reaches zero, remove the chemical from the inventory
        if self.inventory[name]["quantity"] == 0:
            print(f"All quantity of '{name}' has been removed from the inventory.")
            del self.inventory[name]
        return self.inventory

    def update_concentration(self, name, concentration):
        # Check if the chemical exists in the inventory
        if name not in self.inventory:
            print(f"Chemical '{name}' does not exist in the inventory.")
            return
        # Update the concentration of the chemical
        self.inventory[name]["concentration"] = concentration

    def add_quantity(self, name, quantity):
        # Check if the chemical exists in the inventory
        if name not in self.inventory:
            print(f"Chemical '{name}' does not exist in the inventory.")
            return self.inventory
        # Update the quantity of the chemical
        self.inventory[name]["quantity"] += quantity
        return self.inventory

    def print_inventory(self):
        # Print the current inventory
        print("Current Inventory:")
        if not self.inventory:
            print("The inventory is empty.")
        else:
            for chemical, properties in self.inventory.items():
                print(f"Name: {chemical}, Quantity: {properties['quantity']} liters, Concentration: {properties['concentration']}%")

# Example usage
inventory = ChemicalInventory()

# Add chemicals to the inventory
inventory.add_chemical("Chemical A", 10.0, 50.0)
inventory.add_chemical("Chemical B", 20.0, 75.0)

# Print the initial inventory
inventory.print_inventory()

# Remove 5 liters of Chemical A
inventory.remove_chemical("Chemical A", 5.0)
print("\nAfter removing 5 liters of Chemical A:")
inventory.print_inventory()

# Add 10 liters of Chemical B
inventory.add_quantity("Chemical B", 10.0)
print("\nAfter adding 10 liters of Chemical B:")
inventory.print_inventory()

# Update the concentration of Chemical A
inventory.update_concentration("Chemical A", 60.0)
print("\nAfter updating the concentration of Chemical A:")
inventory.print_inventory()

# Remove all quantity of Chemical A
inventory.remove_chemical("Chemical A", 5.0)
print("\nAfter removing all quantity of Chemical A:")
inventory.print_inventory()