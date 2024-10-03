class Trip: 
    def __init__(self, trip_id, destination, date, price): 
        self.trip_id = trip_id
        self.destination = destination
        self.date = date 
        self.price = price 
        
    def display_trip_info(self): 
        print(f"Trip ID: {self.trip_id} | Destination: {self.destination} | Date: {self.date} | Price: ${self.price}")
        
class Booking: 
    def __init__(self, trip, passenger_name): 
        self.trip = trip 
        self.passenger_name = passenger_name
    
    def display_booking_info(self): 
        print(f"Passenger: {self.passenger_name} | Destination: {self.trip.destination} | Date: {self.trip.date} | price: ${self.trip.price}")
        
    
class BookingSystem: 
    def __init__(self): 
        self.trips = [] 
        self.bookings = []
    
    def add_trip(self, trip): 
        self.trips.append(trip)
        
    def view_trips(self): 
        if not self.trips: 
            print("No trips available at the moment.")
            
        else: 
            print("\n ---- Available Trips ----")
            
            for trip in self.trips: 
                trip.display_trip_info() 
                
    def book_trip(self, trip_id, passenger_name): 
        for trip in self.trips:
            if trip.trip_id == trip_id: 
                booking = Booking(trip, passenger_name)
                self.booking.append(booking)
                print(f"\n Booking confirmed for {passenger_name} to {trip.destination} on {trip.date}.") 
                return
        print(f"No trip found with Trip ID {trip_id}. Please try again.")
        
        
    def view_booking(self):
        if not self.bookings:
            print("No bookings have been made yet.")
            
        else: 
            print("\n ---- Bookings Summary -----")
            for booking in self.bookings: 
                booking.display_booking_info()
                
def main(): 
    booking_system = BookingSystem() 
    
    trip1 = Trip(101, "Paris", "2024-12-15", 500)
    trip2 = Trip(102, "Palestine", "2024-1-5", 1500)
    trip3 = Trip(103, "Jordan", "2024-11-20", 800)
    
     
    booking_system.add_trip(trip1)
    booking_system.add_trip(trip2)
    booking_system.add_trip(trip3)
    
    
    while True: 
        print("\n --- Travel Ticket Booking System ---")
        print("1. View Available Trips")
        print("2. Book a Trip")
        print("3. View Bookings")
        print("4. Exit")
        
        choice = input("Choose an option!") 
        
        if choice == "1":
            booking_system.view_trips()
            
        elif choice == "2": 
            passenger_name = input("Enter your name:")
            trip_id = int(input("Enter the trip ID to book: "))
            booking_system.book_trip(trip_id, passenger_name) 
            
        elif choice == "3": 
            booking_system.view_booking()

        elif choice == "4": 
            print("Exiting the system try again.")
            break
        
        else: 
            print("Invalid option, please try again." )
            
            
if __name__ == "__main__":
    main()           
                
                
                       
        
        


