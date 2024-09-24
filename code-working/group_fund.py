import random

def start_group_fund():
    participants = []
    
    num_participants = int(input("Enter the number of participants in the fund: "))
    
    for i in range(num_participants):
        name = input(f"Enter the name of participant #{i + 1}: ")
        participants.append(name)  # Add the participant to the list
    
    amount = 100
    print(f"Each participant must contribute {amount} dollars.")
    
    payment_schedule = [] 
    
    for month in range(1, num_participants + 1): 
        print(f"\nMonth {month}:")
        
        chosen_one = random.choice(participants)
        print(f"{chosen_one} will receive {amount * num_participants} dollars this month.")
        
        payment_schedule.append((chosen_one, month))  # Fix the tuple syntax
        
        participants.remove(chosen_one)  # Remove the chosen participant for the next month
    
    print("\nGroup Fund Schedule:")
    
    for person, month in payment_schedule: 
        print(f"{person} will receive the money in month {month}.")

start_group_fund()
