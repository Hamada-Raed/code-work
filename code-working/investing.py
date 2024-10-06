import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

VALID_CURRENCIES = {
    "USD",
    "CAD",
    "EUR",
    "JPY",
    "GBP",
    "CNY",
    "AUD",
    "SAR",
    "AED",
    "TRY",
}


class Investment:
    def __init__(self, name, ticker, amount, currency):
        self.name = name
        self.ticker = ticker
        self.amount = amount
        self.currency = currency


class InvestmentTracker:
    def __init__(self):
        self.investments = []

    def add_investment(self):
        name = input("Please enter company/startup name: ")
        ticker = input("Please enter ticker symbol: ")

        while True:
            try:
                amount = float(input("Please enter amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            currency = input("Enter currency code (e.g., USD, EUR): ").upper()
            if currency in VALID_CURRENCIES:
                break
            print("Invalid input. Please enter a valid currency code.")

        self.investments.append(Investment(name, ticker, amount, currency))
        print("Investment added successfully.")

    def remove_investment(self):
        self.list_investments()
        index = int(input("Enter the ID of the investment to remove: ")) - 1
        if 0 <= index < len(self.investments):
            del self.investments[index]
            print("Investment removed successfully!")
        else:
            print("Invalid investment ID.")

    def list_investments(self):
        if not self.investments:
            print("No investments to display.")
        else:
            for i, inv in enumerate(self.investments):
                print(f"[{i + 1}]: {inv.name} ({inv.ticker}): {inv.amount} {inv.currency}")

    def load_from_csv(self):
        file_path = self.get_file_path("open")
        if file_path:
            with open(file_path) as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                self.investments = [Investment(*row) for row in reader]
            print("Investments loaded successfully!")
        else:
            print("No file selected.")

    def save_to_csv(self):
        file_path = self.get_file_path("save")
        if file_path:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Ticker", "Amount", "Currency"])
                for inv in self.investments:
                    writer.writerow([inv.name, inv.ticker, inv.amount, inv.currency])
            print("Investments saved successfully.")
        else:
            print("No file selected.")

    def get_file_path(self, mode="open"):
        Tk().withdraw()
        if mode == "open":
            return askopenfilename(filetypes=[("CSV Files", "*.csv")])
        return asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])


def main():
    investment_tracker = InvestmentTracker()

    print("Welcome to this application where you can track your investments!")
    while True:
        print("::Investment Tracker::")
        print("1. Add new investment")
        print("2. Remove an investment")
        print("3. List all investments")
        print("4. Load from CSV file")
        print("5. Save to CSV file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print("*" * 25)
        if choice == "1":
            investment_tracker.add_investment()
        elif choice == "2":
            investment_tracker.remove_investment()
        elif choice == "3":
            investment_tracker.list_investments()
        elif choice == "4":
            investment_tracker.load_from_csv()
        elif choice == "5":
            investment_tracker.save_to_csv()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
        print("*" * 25)


if __name__ == "__main__":
    main()
