import json
import os
from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict


class ProductError(Exception):
    """Custom exception for Product-related errors."""
    pass


@dataclass
class Product:
    """Represents a product in the inventory."""
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        """Validates the product attributes after initialization."""
        if not isinstance(self.name, str) or not self.name:
            raise ProductError("Product name must be a non-empty string.")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ProductError("Product price must be a non-negative number.")
        if not isinstance(self.quantity, int) or self.quantity < 0:
            raise ProductError("Product quantity must be a non-negative integer.")
        
        self.price = float(self.price)


class Inventory:
    """Manages the inventory of products."""
    
    def __init__(self):
        """Initializes an empty inventory."""
        self.products: Dict[str, Dict[str, Any]] = {}

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the inventory.

        Args:
        product (Product): The product to add.

        Raises:
        ProductError: If the product already exists in the inventory.
        """
        if product.name in self.products:
            raise ProductError(f"Product '{product.name}' already exists in the inventory.")
        
        self.products[product.name] = asdict(product)

    def remove_product(self, name: str) -> None:
        """
        Removes a product from the inventory.

        Args:
        name (str): The name of the product to remove.

        Raises:
        ProductError: If the product is not found in the inventory.
        """
        if name not in self.products:
            raise ProductError(f"Product '{name}' not found in inventory.")
        
        del self.products[name]

    def update_product(self, name: str, price: Optional[float] = None, quantity: Optional[int] = None) -> None:
        """
        Updates a product in the inventory.

        Args:
        name (str): The name of the product to update.
        price (float, optional): The new price of the product.
        quantity (int, optional): The new quantity of the product.

        Raises:
        ProductError: If the product is not found or if the input values are invalid.
        """
        if name not in self.products:
            raise ProductError(f"Product '{name}' not found in inventory.")
        
        product_dict = self.products[name]
        
        if price is not None:
            if not isinstance(price, (int, float)) or price < 0:
                raise ProductError("Product price must be a non-negative number.")
            product_dict["price"] = float(price)
        
        if quantity is not None:
            if not isinstance(quantity, int) or quantity < 0:
                raise ProductError("Product quantity must be a non-negative integer.")
            product_dict["quantity"] = quantity

    def get_product(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Gets a product from the inventory.

        Args:
        name (str): The name of the product to get.

        Returns:
        dict: The product data, or None if not found.
        """
        return self.products.get(name)

    def save_to_file(self, filename: str) -> None:
        """
        Saves the inventory to a file.

        Args:
        filename (str): The filename to save to.

        Raises:
        IOError: If there's an error writing to the file.
        """
        try:
            with open(filename, "w") as f:
                json.dump(self.products, f, indent=2)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Loads the inventory from a file.

        Args:
        filename (str): The filename to load from.

        Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If there's an error decoding the JSON data.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")
        
        try:
            with open(filename, "r") as f:
                self.products = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON data: {e}", e.doc, e.pos)


def main():
    inventory = Inventory()
    filename = "inventory.json"

    # Load inventory from file
    try:
        inventory.load_from_file(filename)
        print(f"Inventory loaded from {filename}")
    except FileNotFoundError:
        print(f"No existing inventory file found. Starting with an empty inventory.")
    except json.JSONDecodeError as e:
        print(f"Error loading inventory: {e}")
        return

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. Get Product")
        print("5. Save and Exit")

        try:
            choice = input("Enter your choice: ")
        except EOFError:
            print("\nInput terminated. Exiting program.")
            break

        try:
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                product = Product(name, price, quantity)
                inventory.add_product(product)
                print(f"Product '{name}' added successfully.")
            elif choice == "2":
                name = input("Enter product name: ")
                inventory.remove_product(name)
                print(f"Product '{name}' removed successfully.")
            elif choice == "3":
                name = input("Enter product name: ")
                price_input = input("Enter new product price (press Enter to skip): ")
                quantity_input = input("Enter new product quantity (press Enter to skip): ")
                price = float(price_input) if price_input else None
                quantity = int(quantity_input) if quantity_input else None
                inventory.update_product(name, price, quantity)
                print(f"Product '{name}' updated successfully.")
            elif choice == "4":
                name = input("Enter product name: ")
                product = inventory.get_product(name)
                if product:
                    print(f"Product Name: {name}")
                    print(f"Product Price: {product['price']}")
                    print(f"Product Quantity: {product['quantity']}")
                else:
                    print(f"Product '{name}' not found in inventory.")
            elif choice == "5":
                # Save inventory to file
                inventory.save_to_file(filename)
                print(f"Inventory saved to {filename}")
                break
            else:
                print("Invalid choice. Please try again.")
        except (ProductError, ValueError, IOError) as e:
            print(f"Error: {e}")
        except EOFError:
            print("\nInput terminated. Exiting program.")
            break

if __name__ == "__main__":
    main()