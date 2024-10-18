import json
import os

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    def __init__(self):
        self.products = {}
        self.load_inventory()

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product ID {product.product_id} already exists. Updating existing product.")
            self.update_product(product.product_id, product.quantity, product.price)
        else:
            self.products[product.product_id] = product
            print(f"Product {product.name} added successfully.")

    def update_product(self, product_id, quantity, price):
        if product_id in self.products:
            self.products[product_id].quantity = quantity
            self.products[product_id].price = price
            print(f"Product ID {product_id} updated successfully.")
        else:
            print(f"Product ID {product_id} not found.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product ID {product_id} removed successfully.")
        else:
            print(f"Product ID {product_id} not found.")

    def list_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(f"ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

    def save_inventory(self):
        with open('inventory.json', 'w') as f:
            json.dump({pid: product.to_dict() for pid, product in self.products.items()}, f)
        print("Inventory saved to file.")

    def load_inventory(self):
        if os.path.exists('inventory.json'):
            with open('inventory.json', 'r') as f:
                data = json.load(f)
                for pid, product_data in data.items():
                    product = Product(product_data['product_id'], product_data['name'], product_data['quantity'], product_data['price'])
                    self.products[pid] = product
            print("Inventory loaded from file.")
        else:
            print("No inventory file found. Starting with an empty inventory.")

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. List Products")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                quantity = int(input("Enter product quantity: "))
                price = float(input("Enter product price: "))
                product = Product(product_id, name, quantity, price)
                inventory.add_product(product)

            elif choice == '2':
                product_id = input("Enter product ID to update: ")
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                inventory.update_product(product_id, quantity, price)

            elif choice == '3':
                product_id = input("Enter product ID to remove: ")
                inventory.remove_product(product_id)

            elif choice == '4':
                inventory.list_products()

            elif choice == '5':
                inventory.save_inventory()
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}. Please enter valid input.")

if __name__ == "__main__":
    main()