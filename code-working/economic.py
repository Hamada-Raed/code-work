import random 

class Bank: 
    def __init__(self, initial_balance): 
        self.balance = initial_balance
        self.customers = 1000 
        self.loan_interset_rate = 0.05 
        self.saving_interset_rate = 0.02
        self.economy = 'Stable'
        self.month = 1 
        self.bankrupt = False
        
    def change_economy(self): 
        economic_conditions = ['Inflation', "Recession", "Recovery", "Stable"]
        self.economy = random.choice(economic_conditions)
        print(f'\n Current economic condition: {self.economy}')
        
        if self.economy == "Inflation": 
            self.loan_interset_rate = 0.08
            self.saving_interset_rate = 0.01 
        elif self.economy == "Recession": 
            self.loan_interset_rate = 0.03
            self.saving_interset_rate = 0.05
        elif self.economy == "Recovery": 
            self.loan_interset_rate = 0.06
            self.saving_interset_rate = 0.03
        else: 
            self.loan_interset_rate = 0.05
            self.saving_interset_rate = 0.02
            
    def customer_activity(self): 
        if self.economy == "Inflation": 
            deposite = random.randint(10000, 50000)
            loans = random.randint(20000, 70000)
        elif self.economy == "Recession": 
            deposite = random.randint(15000, 300000)
            loans = random.randint(15000, 400000)
        elif self.economy == "Recession": 
            deposite = random.randint(15000, 400000)
            loans = random.randint(15000, 500000) 
        else: 
            deposite = random.randint(10000, 40000)
            loans = random.randint(15000, 500000) 
            
        self.balance += deposite 
        loan_profit = loans * self.loan_interset_rate
        self.balance += loan_profit 
        
        print(f"\n Customer activity: Deposits: ${deposite}, Loans issued: ${loans} with profit of ${loan_profit: .2f}")

    def pay_saving_interset(self): 
        interset_payment = self.customers * self.saving_interset_rate * 100 
        self.balance -= interset_payment
        print(f"\n Saving interset payment to customers: ${interset_payment: .2f}")
        
    def make_decision(self):
        print("\n Banking Decisions:")        
        print("1. Increase marketing to attact new customers.")        
        print("2. Invest in technology to improve operations.")        
        print("3. Reduce Loan interset rates to attack more borrowers.")        
        print("4. Increase savings interset rates to attact more deposits.")        
        choice = input("Choose Your strategy (1,2,3, or 4): ")
        
        
        if choice == "1": 
            new_customers = random.randint(50, 200)
            self.customers += new_customers
            print(f"\n You attracted {new_customers} new cutsomers.")
            
        elif choice == "2": 
            inverstment_cost = random.randint(5000, 20000)
            self.balance -= inverstment_cost
            print(f"\n You invested ${inverstment_cost} in new technology")
            
        elif choice == "3": 
            self.loan_interset_rate += 0.01 
            print(f"\n You increase the savings interest rate to {self.saving_interset_rate: .2f}")
            
        else: 
            print("Invalid choice, no action taken.")
            
    
    def end_of_month(self): 
        print(f"\n End of month {self.month}. Bank balance: {self.balance: .2f}.")
        if self.balance < 0 : 
            self.bankrupt = True
            print("\n The bank is bankrupt!")
        self.month += 1 
        
    def play_game(self):
        print(f"Starting balance: ${self.balance: .2f}, Customers: {self.customers}.")
        
        while not self.bankrupt and self.month <= 12: 
            self.change_economy()
            self.customer_activity()
            self.pay_saving_interset()
            self.make_decision
            self.end_of_month()
            
        if not self.bankrupt: 
            print(f"\n Congratualtions! You successfully managed the bank for a year.")
            
        else: 
            print("Game over. Your bank went bankrupt")
            
            
def start_game():
    print("Welcome to the Economic Bank Simulation!")
    initial_balance = 10000
    bank = Bank(initial_balance)
    
start_game() 
    
    
    
    