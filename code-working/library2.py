class Book:
    def __init__(self, title, author, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_quantity(self, title, quantity):
        for book in self.books:
            if book.title == title:
                if book.quantity + quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                book.quantity += quantity
                return
        print("Book not found.")

    def view_inventory(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}, Quantity: {book.quantity}")

    def calculate_total_value(self):
        return sum(book.price * book.quantity for book in self.books)

# Example usage:
inventory = Inventory()
book1 = Book("Book Title 1", "Author 1", 15.99, 0)
inventory.add_book(book1)
inventory.view_inventory()
