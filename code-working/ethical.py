import random

# Define the Employee class to represent each bank employee
class Employee: 
    def __init__(self, name): 
        self.name = name 
        self.balance = 1000  # Starting virtual money for each employee
        self.integrity_score = 100 # Initial integrity score
    
    
    #Method for the employee to preform a financial task
    def perform_task(self): 
        #Randomly select a task for the employee to perform 
        task = random.choice(['loan', 'investment', 'unethical'])
        # If the task ia a loan, the employee grants a loan and increase balance.  
        if task == "loan": 
            print(f"{self.name} is granting a loan.")
            self.balance += random.randint(50, 200)
            
        # If the task is an inerstment, the employee makes an investment 
        elif task == "investment": 
            print(f"{self.name} is making an investment.")
            # Investment can either succedd pr faol affecting the balance 
            if random.choice([True, False]): 
                # Successful investment 
                self.balance += random.randint(100, 500)
            else: 
                # Failed investment 
                self.balance -= random.randint(50, 200)
        elif task == "unethical": 
            # If the task is unthical, the employee daces an ethical chaalenge 
            print(f"{self.name} has encountered an unethical opportunity.")
            # Randomly decide if the empoyee acts ethically or not. 
            if random.choice([True, False]): 
                print(f"{self.name} acted ethically.")
                self.integrity_score += 10 # Reward for acting ethically 
            else: 
                print(f"{self.name} acted unethically.")
                self.integrity_score -= 20 # Panalty for unethical behavior 
                # Unethical behavior can increase the employee's balance
                self.balance += random.randint(200, 1000)

# main function to run the game simulation
def main():
    print("Welcome to Virtual Bank Manager!")
    # Create a list of employees to participate in the game. 
    employees = [Employee('Hamada'), Employee("Yara"), Employee('Ahmad')]
    
    # Simulate a set fnumber of rounds where employees perform tasks 
    for round in range(3):  # 3 rounds in this example
        for emp in employees: 
            emp.perform_task()
    
    # Evaluate and display the results at the end of game 
    print('\n --- Result ---')
    for emp in employees: 
        print(f"{emp.name} - Balance: ${emp.balance}, Integrity Score: {emp.integrity_score}")
        
        # check if the employee has showen signs of unethical behavior 
        if emp.integrity_score < 80: 
            print(f"{emp.name} might be involved in unethical behavior.")
        else: 
            print(f"{emp.name} is managing funds responsibly.")
                
# Entry point of the script. 
if __name__ == '__main__':
    main()        
