class Trip: 
    def __init__(self, name, destination, date, cost_per_person): 
        self.name = name 
        self.destination = destination 
        self.date = date 
        self.cost_per_person = cost_per_person
        self.passengers = []
        self.expenses = [] 
        
    def add_passenger(self, passenger_name): 
        self.passengers.append(passenger_name) 
        print(f"Passenger {passenger_name} added to {self.name}") 
        
    def remove_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            print(f"Passenger {passenger_name} removed from {self.name}")
        else: 
            print(f"Passenger {passenger_name} not found.")
            
    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount}) 
        print(f"Expense '{description}' of {amount}$ added to {self.name}")
        
    def calculate_total_cost(self): 
        return len(self.passengers) * self.cost_per_person
    
    def calculate_total_expenses(self): 
        return sum(expense['amount'] for expense in self.expenses)
    
    def calculate_total_revenue(self): 
        return self.calculate_total_cost()
    
    def get_trip_summary(self): 
        return {
            "name": self.name, 
            "destination": self.destination, 
            "date": self.date,
            "passengers": len(self.passengers), 
            "total_cost": self.calculate_total_cost(), 
            "total_expenses": self.calculate_total_expenses(), 
            "profit_or_loss": self.calculate_total_revenue() - self.calculate_total_expenses()
        }
        
class Finance: 
    def __init__(self):
        self.trips = []
        
    def add_trip(self, trip): 
        self.trips.append(trip)
        print(f"Trip {trip.name} to {trip.destination} added.")
        
    def view_trips(self): 
        if not self.trips: 
            print("No trips found.")
        for trip in self.trips: 
            summary = trip.get_trip_summary()
            print(f"Trip: {summary['name']}, Destination: {summary['destination']}, Date: {summary['date']}")
            print(f"Passengers: {summary['passengers']}, Total Cost: {summary['total_cost']}, Total Expenses: {summary['total_expenses']}$") 
            print(f"Profit/Loss: {summary['profit_or_loss']}$")
            print("-" * 30) 
            
    def generate_financial_report(self): 
        total_revenue = sum(trip.calculate_total_revenue() for trip in self.trips)
        total_expenses = sum(trip.calculate_total_expenses() for trip in self.trips)  # Corrected method name
        total_profit_or_loss = total_revenue - total_expenses 
        print(f"Total Revenue: {total_revenue}$, Total Expenses: {total_expenses}$")
        print(f"Overall Profit/Loss: {total_profit_or_loss}$")
        print("-" * 30)

def main():
    finance_system = Finance()
    
    while True: 
        print("\n -- Travel Agency Financial Management --")
        print("1. Add a new trip")            
        print("2. View all trips")            
        print("3. Add passenger to trip")            
        print("4. Add expense to trip")            
        print("5. Generate financial report")            
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1": 
            name = input("Enter trip name: ") 
            destination = input("Enter trip destination: ")
            date = input("Enter trip date (YYYY-MM-DD): ")
            cost_per_person = float(input("Enter cost per person (USD): "))
            trip = Trip(name, destination, date, cost_per_person)
            finance_system.add_trip(trip)
            
        elif choice == "2": 
            finance_system.view_trips()
            
        elif choice == "3": 
            trip_name = input("Enter trip name: ")
            for trip in finance_system.trips: 
                if trip.name == trip_name: 
                    passenger_name = input("Enter passenger name: ")
                    trip.add_passenger(passenger_name) 
                    break 
            else: 
                print(f"Trip {trip_name} not found.")
                
        elif choice == "4": 
            trip_name = input("Enter trip name: ")
            for trip in finance_system.trips: 
                if trip.name == trip_name: 
                    description = input("Enter expense description: ")
                    amount = float(input("Enter expense amount (USD): "))
                    trip.add_expense(description, amount)
                    break
            else: 
                print(f"Trip {trip_name} not found.")
                
        elif choice == "5": 
            finance_system.generate_financial_report() 
            
        elif choice == "6": 
            print("Exiting system...")
            break
        
        else: 
            print("Invalid option, please try again!")
            
if __name__ == "__main__": 
    main()
