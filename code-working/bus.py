
# Initiazlize the User class
class User: 
    def __init__(self, name, balance):
        """
            Initialize the User object with a name and balance
            Parameters:
            name : the name of the user 
            balance : The initial balance of the user   
        """
        self.name = name
        self.balance = balance
        
    def deduct_balance(self, amount): 
        """ Deduct the given amount from the user's balance if sufficient funds exist 
            parameter: 
                amount: the amount to be deducted. 
                
            Returns: 
                bool: True if the deduction is successful, False otherwise. 
        """
        if self.balance >= amount: 
            self.balance -= amount
            print(f"{self.name} paid {amount}. Remaing balance: {self.balance}.")
            return True
        else: 
            print(f"Sorry insufficient balance. Current balance: {self.balance}")
            return False
        
        
    def recharge_balance(self, amount):
        """
            Recharge the user's balance by adding the specified amount.
            Parameter: 
                amount: The amount to be addded for the user balance. 
        """ 
        self.balance += amount
        print(f"{amount} has been recharged to {self.name}'s account. Current balance {self.balance}")
        
        
class Bus: 
    
    """
        Initialize the bus object with a route and price for the fare 
        parameters: 
            rount: The route of the bus 
            price: the fare of the bus ride. 
    """
    def __init__(self, route, price): 
        self.route = route 
        self.price = price 
        
        
    def borad_user(self, user):
        """
            Attempt to board the user onto the bus by deducting the fare from their balance.
            parameter: 
                user: the user attempting to board the bus. 
        """ 
        print(f"{user.name} is trying to board the bus on route: {self.route}")
        if user.deduct_balance(self.price): 
            print(f"{user.name} has boarded the bus on route {self.route}")
            
        else: 
            print(f"{user.name} connot board the bus due to insufficiant balance.") 
 
 
 
            
user1 = User(name='Hamada', balance=50)
bus1 = Bus(route="A to B", price=20)
bus2 = Bus(route="B to C", price=15)
bus1.borad_user(user1) 
bus2.borad_user(user1) 
user1.recharge_balance(30)
bus1.borad_user(user1)

