class Reservation: 
    def __init__(self, reservation_id, customer_name, service_type, time_slot):
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.service_type = service_type 
        self.time_slot = time_slot 
        
    def display_reservation_info(self): 
        print(f"Reservation ID: {self.reservation_id} | Customer: {self.customer_name} | Service: {self.service_type} | Time Slot: {self.time_slot}")
        
class BankReservationSystem:
    def __init__(self): 
        self.available_time_slots = ["09:00 AM", "10:00AM" , "11:00AM" , "12:00AM" , "1:00PM" , "02:00PM" , "03:00PM"]
        self.reservation = [] 
           
    def view_available_time_slots(self):
        if not self.available_time_slots: 
            print("No available time slots left for today. ")
            
        else: 
            print("\n ----Available Time Slots----")
            for slot in self.available_time_slots: 
                print(slot) 
                           
    def make_reservation(self, customer_name, service_type, time_slot): 
        if time_slot in self.available_time_slots: 
            reservation_id = len(self.reservation) + 1 
            reservation = Reservation(reservation_id, customer_name, service_type, time_slot)
            self.reservation.append(reservation)
            self.available_time_slots(time_slot) 
            print(f"\n Reservation confimed for {customer_name} at {time_slot}")
        
        else: 
            print(f"Time Slot {time_slot} is not available. Plase choose a different time.")
            
    def view_reservation(self): 
        if not self.reservation: 
            print("No reservations have been made.") 
            
    
    
            