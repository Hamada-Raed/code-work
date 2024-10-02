class Trip: 
    def __init__(self, name, destination, date, cost_per_person): 
        self.name = name
        self.destination = destination 
        self.date = date 
        self.cost_per_person = cost_per_person 
        self.passengers = [] 
        
    def add_passenger(self, passenger_name): 
        self.passengers.append(passenger_name)
        
    def calculate_total_cost(self): 
        return len(self.passengers) * self.cost_per_person
    
class Finance: 
    def __init__(self):  
        self.expenses = 0
        self.revenue = 0 
        
    def add_expense(self, amount): 
        self.expenses += amount 
        
    def add_revenue(self, amount): 
        self.revenue += amount 
        
    def calculate_profit(self): 
        return self.revenue - self.expenses 
    
def main(): 
    trip1 = Trip("Trip to Paris", "Paris", "2024-10-15", 200) 
    
    trip1.add_passenger("Hamada Raed")
    trip1.add_passenger("Nehal Amar")
    
    total_cost = trip1.calculate_total_cost()
    print(f"Total cost for {trip1.name}: {total_cost}$") 
    
    finance = Finance() 
    
    finance.add_revenue(total_cost)
    
    finance.add_expense(500) 
    finance.add_expense(300)
    
    profit = finance.calculate_profit()
    print(f"Net profit/loss: {profit}$")
    
    
if __name__ == "__main__": 
    main()
