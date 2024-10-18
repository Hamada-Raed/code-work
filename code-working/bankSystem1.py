# class BankAccount:
#     def __init__(self, owner, balance):
#         """
#         Initialize the bank account with owner's name and initial balance.
#         """
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         """
#         Deposit a certain amount into the account.
#         """
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         """
#         Withdraw a certain amount from the account. Does not allow negative balance.
#         """
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds.")

#     def check_balance(self):
#         """
#         Return the current balance of the account.
#         """
#         print(f"Current balance: {self.balance}")
#         return self.balance

# # Main function
# def main():
#     # Create a new account with a starting balance of 500
#     account = BankAccount("John Doe", 500)

#     # Perform a series of transactions
#     account.deposit(200)
#     account.withdraw(100)
#     account.withdraw(700)  # This should fail due to insufficient funds
#     account.deposit(-50)   # This is invalid but no check exists in the code
#     account.check_balance()

#     # Invalid test cases
#     account.withdraw("fifty")  # Should raise an error but no handling exists
#     account.deposit("two hundred")  # Should raise an error but no handling exists

# if __name__ == "__main__":
#     main() 

class BankAccount:
    def __init__(self, owner, balance=0):
        """
        Initialize the bank account with owner's name and initial balance.
        Ensure balance is non-negative during initialization.
        """
        self.owner = owner
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Initial balance must be a non-negative number.")
        
    def deposit(self, amount):
        """
        Deposit a certain amount into the account.
        Only accept positive numerical values.
        """
        if isinstance(amount, (int, float)) and amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    
    def withdraw(self, amount):
        """
        Withdraw a certain amount from the account.
        Ensure the balance does not become negative.
        """
        if isinstance(amount, (int, float)) and amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrawn {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        """
        Return the current balance of the account.
        """
        print(f"Current balance: {self.__balance}")
        return self.__balance

def main():
    try:
        # Create a new account with a starting balance of 500
        account = BankAccount("John Doe", 500)

        # Perform a series of transactions
        account.deposit(200)
        account.withdraw(100)
        account.withdraw(700)  # This should fail due to insufficient funds
        account.deposit(-50)   # This will be rejected as invalid
        account.check_balance()

        # Invalid test cases
        account.withdraw("fifty")  # This will be rejected due to invalid input type
        account.deposit("two hundred")  # This will be rejected due to invalid input type
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()