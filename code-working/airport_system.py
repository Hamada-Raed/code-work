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
            self.status = "On Time"
        else:
            self.status = "Scheduled"

    def display_flight_info(self):
        time_left = (self.departure_time - datetime.now()).total_seconds() / 60
        time_left_str = f"{int(time_left // 60)}h {int(time_left % 60)}m" if time_left > 0 else "Departed"

        print(f"\nFlight: {self.flight_no}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time.strftime('%H:%M')} ({time_left_str} remaining)")
        print(f"Gate: {self.gate}")
        print(f"Status: {self.status}")
        print("-" * 30)


class AirportDispalySystem:
    def __init__(self):
        self.flights = [
            Flight("AB123", "London", datetime.now() + timedelta(minutes=60), "Gate A1", "Scheduled"),
            Flight("CD456", "New York", datetime.now() + timedelta(minutes=90), "Gate B2", "Scheduled"),
            Flight("EF789", "Palestine", datetime.now() + timedelta(minutes=120), "Gate C3", "Scheduled"),
        ]
        self.current_flight = 0

    def display_all_flights(self, flight_no=None):
        if flight_no:
            # Display information of a specific flight
            for flight in self.flights:
                if flight.flight_no == flight_no:
                    flight.display_flight_info()
                    return
            print(f"Flight {flight_no} not found")
        else:
            # Display all flights
            for flight in self.flights:
                flight.display_flight_info()

    def update_flight_info(self):
        for flight in self.flights:
            flight.gate = f"Gate {chr(ord(flight.gate[-2]) + 1)}{flight.gate[-1]}"
            flight.departure_time += timedelta(minutes=10)

    def start_display(self):
        while True:
            print("\033[H\033[J", end="")
            print("** Airport Flight Information")
            self.display_all_flights()

            user_input = input("\nEnter 'D' to view detailed flight info, 'U' to update flight data, or 'Q' to Quit: ")
            if user_input == "D":
                flight_no = input("\nEnter flight number to view details: ")
                self.display_all_flights(flight_no)
            elif user_input == "U":
                self.update_flight_info()
                print("\nFlight data updated")
            elif user_input == "Q":
                print("\nExiting system")
                break

            time.sleep(5)


if __name__ == "__main__":
    airpost_system = AirportDispalySystem()
    airpost_system.start_display()
