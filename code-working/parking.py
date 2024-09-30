import time 
import datetime 


class ParkingTicket: 
    def __init__(self): 
        self.entry_time = None 
        self.exit_time = None
        self.amount_due = 0.0
        self.is_paid = False 
        
    def enter_parking(self): 
        self.entry_time = datetime.datetime.now()
        print(f"Car entered at {self.entry_time.strftime('%y-%m-%d %H:%M:%S')}\n") 
        
    def exit_parking(self): 
        if self.entry_time:
            self.exit_time = datetime.datetime.now()
            print(f"Car exited at {self.exit_time.strftime('%y-%m-%d %H:%M:%S')}\n") 
            self.calculate_fee() 
        
        else:
            print("Error: Car has not entered the parking lot yet.\n") 
            
    def calculate_fee(self): 
        duration = (self.exit_time - self.entry_time).total_seconds() / 3600
        rate_per_hour = 5.00 
        self.amount_due = round(duration * rate_per_hour, 2)
        print(f"Parking duration: {round(duration, 2)} hours")
        print(f"Amount to pay: ${self.amount_due}") 
        
    def make_payment(self): 
        if not self.is_paid: 
            print(f"Amount to pay: ${self.amount_due}")
            confirmation = input("Confirm payment (yes/no)? ").lower()
            
            if confirmation == "yes": 
                self.is_paid = True
                print("Payment successful. Thank you!\n")

            else: 
                print("Payment cancelled.\n") 
                
        else: 
            print("Payment already made.\n") 
            
            
def parking_system(): 
    ticket = ParkingTicket() 
    
    while True: 
        print ("Parking System Menu:")       
        print ("1. Enter Parking")       
        print ("2. Exit Parking")       
        print ("3. Make Payment")       
        print ("4. Quit") 
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1": 
            ticket.enter_parking()
            
        elif choice == "2": 
            ticket.exit_parking() 
            
        elif choice == "3": 
            ticket.make_payment() 
            
        elif choice == "4": 
            print("Exiting system. Goodbye!")
            break
        
        else: 
            print("Invalid option. Please try again.\n")
                

parking_system()
