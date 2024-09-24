import random 

def spin_whell():
    options = ["You won 100$", "You won 50$", "Better Luck Next Time", "Better Luck Next Time", "Better Luck Next Time"]
    
    result = random.choice(options)
    return result 

def play_game(): 
    print("Welcome to the Spin Wheel Game!")
    bet_amount = float(input("Enter the amount of moeny you want to bet: "))
    
    result = spin_whell()
    print(f"Spin result: {result}")
    
    if "100" in result: 
        winnings = bet_amount + 100 
    elif "50" in result: 
        winnings = bet_amount + 50
    else: 
        winnings = 0
        print("Better luck next time, try again!")
        
    if winnings > 0: 
        print(f"Congratulations you won: ${winnings}")
    else: 
        print("Unfortunately, you did not win anything this time!")
        
        
play_game()