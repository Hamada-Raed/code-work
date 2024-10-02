import time 
from datetime import datetime, timedelta 

class Flight: 
    def __init__(self, flight_no, destination, departure_time, gate, status):  # Corrected __init__ here
        self.flight_no = flight_no 
        self.destination = destination 
        self.departure_time = departure_time 
        self.gate = gate 
        self.status = status
        
    
    def display_flight_info(self): 
        print(f"\n Flight: {self.flight_no}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time.strftime('%H:%M')}")
        print(f"Gate: {self.gate}")
        print(f"Status: {self.status}")
        print("-" * 30)
        
class AirportDisplaySystem: 
    def __init__(self): 
        self.flights = [
            Flight("AB123", "London", datetime.now() + timedelta(minutes=60), "Gate A1", "On Time"), 
            Flight("CD435", "New York", datetime.now() + timedelta(minutes=90), "Gate B1", "Boarding"), 
            Flight("EF789", "London", datetime.now() + timedelta(minutes=120), "Gate A1", "Delaying"), 
        ]
        self.current_flight = 0
        
    def start_display(self): 
        while True: 
            print('\003[H\033[J', end="") 
            flight = self.flights[self.current_flight]
            flight.display_flight_info()
            
            time.sleep(5)
            self.current_flight = (self.current_flight + 1) % len(self.flights) 
            
if __name__ == "__main__": 
    airport_system = AirportDisplaySystem()
    airport_system.start_display()
