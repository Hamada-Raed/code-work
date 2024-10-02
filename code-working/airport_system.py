import time
from datetime import datetime, timedelta 


class Flight: 
    def __init__(self, flight_no, destination, departure_time, gate, status): 
        self.flight_no = flight_no
        self.destination = destination
        self.departure_time = departure_time 
        self.gate = gate 
        self.status = status 
        
        
    def update_status(self): 
        time_left = (self.departure_time - datetime.now()).total_seconds() / 60
        
        if time_left <= 0: 
            self.status = "Departed" 
            
        elif time_left <= 10: 
            self.status = "Boarding"
            
        elif time_left <= 30: 
            self.status = "Final Call"
            
        elif time_left <= 60: 
            self.status = " On Time"
            
        else: 
            self.status = "Scheduled"
            
    def display_flight_info(self): 
        time_left = (self.departure_time - datetime.now()).total_seconds() / 60 
        time_left_str = f"{int(time_left // 60)}h {int(time_left % 60)}m" if time_left > 0 else "Departed" 
        
        print(f"\n Flight: {self.flight_no}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time.strftime('%H:%M')} ({time_left_str} remaining)") 
        
        
        
class AirportDispalySystem: 
    def __init__(self):
        self.flights = [
            
        ]
        