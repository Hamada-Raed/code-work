import random 

class Player: 
    def __init__(self, loan_amount, interest_rate, loan_term):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.load_term = loan_term
        self.remaining_load = loan_amount
        self.balance = loan_term 
        self.monthly_payment = (loan_term * (1 + interest_rate)) / loan_term
        self.bankrupt = False
        self.month = 1 
        
    def invest(self): 
        print("\n You have received a loan of {:.2f}. You can invest in a project.".format(self.loan_amount))
        print("Investment options:")
        print("1. Open a small business")
        print("2. Buy a house for rental income")
        print("3. Stock market investment(High risk)")
        choice = input("Choose your investment (1,2, or 3): ")
        
        if choice == "1": 
            print("\n You invested in a small business.")
            self.business_income() 
            
        elif choice == "2": 
            print("\n Buy a house for rental income.")
            self.business_income() 
            
        elif choice == "3": 
            print("\n Stock market investment(High risk).")
            self.stock_market_income()
        else: 
            print("Invalid choice. No investment made.")
            self.invest() 
            
    def business_income(self): 
        income = random.randint(2000, 5000)
        print(f'\n Your small business generates ${income} per month.')
        self.balance += income 
        
    def house_income(self):
        income = random.randint(1000, 3000)
        print(f"\n YOu rental income is ${income} per month.")
        
    def stock_market_income(self): 
        if random.random() > 0.5: 
            income = random.randint(5000, 100000)
            print(f"\n You made a great profit from the stock market! Income ${income}.")
        else: 
            income = -random.randint(2000, 5000)
            print(f"\n The stock market crashed! You lost ${abs(income)}.")
        self.balance += income
        
    def make_payment(self): 
        if self.balance >= self.monthly_payment: 
            self.balance -= self.monthly_payment 
            self.remaining_load -= self.monthly_payment
            print(f"\n Month {self.month}. You paid ${self.monthly_payment: .2f} towards your loan. Remaining load ${self.remaining_load: .2f}")

        else: 
            print('\n You could not make the loan payment. you are bankrupt')

    def end_of_month(self):
        print(f'\n End of month {self.month}. Your balance is: ${self.balance : .2f}')
        self.month += 1 
            
    def paly_game(self): 
        self.invest() 
        
        while self.month <= self.load_term and not self.bankrupt: 
            self.make_payment() 
            if not self.bankrupt: 
                self.end_of_month() 
                
        if self.bankrupt: 
            print("\n Game over. You went bankrupt")
        else: 
            print('\n Congratulation! You have successfully repaid your loan.')
            

def start_game(): 
    print("Welcome to the Load Repayment Simulation!")
    loan_amount = 1000
    interest_rate = 0.1 
    loan_term = 12 
    
    
    player = Player(loan_amount, interest_rate, loan_term)
    player.paly_game() 
    
    
start_game()
            
                