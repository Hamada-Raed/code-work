class Payment: 
    def __init__(self, amount): 
        self.amount = amount
        
    def process_payment(self): 
        raise NotImplementedError("Subclasses must implement this method!")
    
    def receipt(self): 
        print(f"Payment of ${self.amount} has been processed.")
        
        
class CrediCardPayment(Payment): 
    def __init__(self, amount, card_number, card_holder, expiry_date):
        super().__init__(amount) 
        self.card_number = card_number
        self.card_holder = card_holder 
        self.expiry_date = expiry_date

    def process_payment(self):
        if self._validate_card():
            print(f"Processing Credit Card payment for {self.card_holder}.")
            self.receipt()
        else: 
            print("Invalid credit card details.")
            
    def _validate_card(self): 
        if len(self.card_number) == 16 and self.expiry_date > "2024-01": 
            return True 
        return False
    
    
class PayPalPayment(Payment): 
    def __init__(self, amount, email): 
        super().__init__(amount)
        self.email = email
        
    def process_payment(self):
        print(f"Processing PayPal payment for {self.email}")
        self.receipt() 
        
class BankTransferPayment(Payment): 
    def __init__(self, amount, bank_account):
        super().__init__(amount)
        self.bank_account = bank_account
        
    def process_payment(self):
        print(f"Processing Bank Transfer payment for account {self.bank_account}")
        self.receipt() 
          
class PaymentGateway: 
    def __init__(self): 
        self.payments = [] 
        
    def add_payment(self, payment): 
        if isinstance(payment, Payment): 
            self.payments.append(payment)
        else: 
            print("Invalid payment type!")
            
    def process_all_payments(self): 
        for payment in self.payments: 
            payment.process_payment()  
            
def main(): 
    credit_payment = CrediCardPayment(200, "1234567890123456", "Hamada", "2025-01")
    paypal_payment = PayPalPayment(100, "Hamada@gmail.com")
    bank_payment = BankTransferPayment(150, "8456456845")
    
    gateway = PaymentGateway()
    gateway.add_payment(credit_payment)
    gateway.add_payment(paypal_payment)
    gateway.add_payment(bank_payment)  # Corrected line
    
    gateway.process_all_payments() 
    
if __name__ == "__main__": 
    main()
