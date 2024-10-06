import cvs 
from datetime import datetime 

def record_transaction(amount, transcation_type): 
    with open('transcations.cvs', mode="a", newline="") as file: 
        writer = cvs.writer(file) 
        date_time = datetime.now().strftime("%Y -%m-%d %H:%M:%S")
        writer.writerow([date_time, transcation_type, amount]) 
        
    print(f"{transcation_type.capitalize()} of {amount} recorded.") 
    
    
def calculate_balance():
    balance = 0 
    
    try: 
        with open('transcations.cvs', mode="r") as file: 
            reader = cvs.reader(file) 
            for row in reader: 
                if row[1] == "cash_in": 
                    balance += float(row[2])
                elif row[1] == "cash_out": 
                    balance += float(row[2])
    except FileNotFoundError: 
        print("No transactions found. ")
        
    return balance 

def pay_salary(employee_name, salary_amount):
    balance = calculate_balance()
    if salary_amount > balance: 
        print(f"Insufficient balance to pay {employee_name}'s salary.")
        
    else: 
        record_transaction(salary_amount, "cash_out")
        print(f"Paid {salary_amount} to {employee_name}")
        
def display_transcations():
    try: 
        with open("transcations.cvs", mode="r") as  file: 
            reader = cvs.reader(file)
            print(f"\n {'Date:' :<20}{'Type' :<10}{'Amount'}")
            print('-' * 40)
            
            for row in reader: 
                print(f"{row[0]:<20}{row[1]:<10}{row[2]}")
                
                
                
    except FileNotFoundError: 
        print('No transactions found. ') 
        
        
def main(): 
    while True: 
        print("\n Financial Management System")
        print("1. Record Transaction")
        print("2. Check Balance ")
        print("3. Pay Salary")
        print("4. Display Transactions ")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        
        
        if choice == "1": 
            transcation_type = input('Enter transaction type (cash_in/cash_out): ').lower()
            amount = float(input("Enter the amount: "))
            record_transaction(amount, transcation_type) 
            
        elif choice == "2": 
            print(f"Current Balance: {calculate_balance()}") 
            
        elif choice == "3": 
            employee_name = input("Enter employee name: ")
            salary_amount = float(input(f"Enter salary amount for {employee_name}: "))
            pay_salary(employee_name, salary_amount)
            
        elif choice == "4": 
            display_transcations() 
            
        elif choice == "5": 
            print("Exiting the system. ")
            
        else: 
            print("Invalid option. Please try again. ")
            
            
if __name__ == "__main__": 
    main()
            