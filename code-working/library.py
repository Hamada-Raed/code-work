class Book:
    """
    A class to represent a book in the inventory.
    
    Attributes:
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    price : float
        The price of the book.
    quantity : int
        The quantity of the book in stock.
    """
    
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    """
    A class to manage the bookstore inventory.
    
    Methods:
    -------
    add_book(title, author, price, quantity):
        Adds a new book to the inventory.
    update_quantity(title, quantity_change):
        Updates the quantity of a book in the inventory.
    view_inventory():
        Returns a list of all books in the inventory.
    calculate_total_value():
        Calculates the total value of the inventory.
    """
    
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        new_book = Book(title, author, price, quantity)
        self.books.append(new_book)
        print(f"Added book: {new_book}")

    def update_quantity(self, title, quantity_change):
        for book in self.books:
            if book.title == title:
                if book.quantity + quantity_change < 0:
                    raise ValueError("Quantity cannot be negative.")
                book.quantity += quantity_change
                print(f"Updated book: {book}")
                return
        print("Book not found in inventory.")

    def view_inventory(self):
        if not self.books:
            print("Inventory is empty.")
        for book in self.books:
            print(book)

    def calculate_total_value(self):
        total_value = sum(book.price * book.quantity for book in self.books)
        print(f"Total inventory value: ${total_value:.2f}")
        return total_value


def main():
    inventory = Inventory()
    
    # Example usage
    try:
        inventory.add_book("The Great Gatsby", "F. Scott Fitzgerald", 10.99, 5)
        inventory.add_book("1984", "George Orwell", 8.99, 0)
        inventory.view_inventory()
        inventory.update_quantity("1984", 5)
        inventory.view_inventory()
        inventory.calculate_total_value()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()