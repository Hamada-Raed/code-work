class Reservation:
    """
    A class to represent a bank reservation (appointment).
    Attributes:
    ----------
    reservation_id : int
        Unique identifier for each reservation.
    customer_name : str
        Name of the customer who made the reservation.
    service_type : str
        Type of service the customer is reserving (e.g., Loan, Account Opening).
    time_slot : str
        The selected time slot for the reservation.
 
    Methods:
    -------
    display_reservation_info():
        Prints out the reservation information (ID, customer name, service, and time slot).
    """
 
    def __init__(self, reservation_id, customer_name, service_type, time_slot):
        """
        Initialize the Reservation object with reservation details.
 
        Parameters:
        ----------
        reservation_id : int
            Unique identifier for the reservation.
        customer_name : str
            The name of the customer making the reservation.
        service_type : str
            The service the customer is reserving (e.g., Loan, Account Opening).
        time_slot : str
            The time slot chosen by the customer for their appointment.
        """
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.time_slot = time_slot
 
    def display_reservation_info(self):
        """Displays the reservation information."""
        print(f"Reservation ID: {self.reservation_id} | Customer: {self.customer_name} | Service: {self.service_type} | Time Slot: {self.time_slot}")
 
 
class BankReservationSystem:
    """
    A class to manage bank reservations.
 
    Attributes:
    ----------
    available_time_slots : list
        A list of available time slots for reservations.
    reservations : list
        A list of Reservation objects that stores all customer reservations.
 
    Methods:
    -------
    view_available_time_slots():
        Displays the available time slots for reservations.
    make_reservation(customer_name, service_type, time_slot):
        Allows a customer to reserve a time slot for a service.
    view_reservations():
        Displays all the reservations made so far.
    """
 
    def __init__(self):
        """Initialize the BankReservationSystem with available time slots and an empty list of reservations."""
        self.available_time_slots = ["09:00 AM", "10:00 AM", "11:00 AM", "01:00 PM", "02:00 PM", "03:00 PM"]
        self.reservations = []
 
    def view_available_time_slots(self):
        """Displays the available time slots for reservations."""
        if not self.available_time_slots:
            print("No available time slots left for today.")
        else:
            print("\n--- Available Time Slots ---")
            for slot in self.available_time_slots:
                print(slot)
 
    def make_reservation(self, customer_name, service_type, time_slot):
        """
        Allows a customer to make a reservation for a specific time slot.
 
        Parameters:
        ----------
        customer_name : str
            The name of the customer making the reservation.
        service_type : str
            The type of service the customer is reserving (e.g., Loan, Account Opening).
        time_slot : str
            The time slot selected by the customer for the reservation.
        """
        if time_slot in self.available_time_slots:
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(reservation_id, customer_name, service_type, time_slot)
            self.reservations.append(reservation)
            self.available_time_slots.remove(time_slot)
            print(f"\nReservation confirmed for {customer_name} at {time_slot}.")
        else:
            print(f"Time slot {time_slot} is not available. Please choose a different time.")
 
    def view_reservations(self):
        """Displays all reservations made by customers."""
        if not self.reservations:
            print("No reservations have been made.")
        else:
            print("\n--- Reservations Summary ---")
            for reservation in self.reservations:
                reservation.display_reservation_info()
 
 
def main():
    """
    Main function to run the bank reservation system.
 
    Allows the user to interact with the system to:
    - View available time slots.
    - Make a reservation.
    - View existing reservations.
    - Exit the system.
    """
    # Initialize the bank reservation system
    reservation_system = BankReservationSystem()
 
    while True:
        print("\n--- Bank Reservation System ---")
        print("1. View Available Time Slots")
        print("2. Make a Reservation")
        print("3. View All Reservations")
        print("4. Exit")
 
        choice = input("Choose an option: ")
 
        if choice == "1":
            # View available time slots
            reservation_system.view_available_time_slots()
 
        elif choice == "2":
            # Make a reservation
            customer_name = input("Enter your name: ")
            service_type = input("Enter the service type (e.g., Loan, Account Opening, Financial Advice): ")
            time_slot = input("Enter the desired time slot (e.g., 09:00 AM): ")
            reservation_system.make_reservation(customer_name, service_type, time_slot)
 
        elif choice == "3":
            # View all reservations
            reservation_system.view_reservations()
 
        elif choice == "4":
            print("Exiting the system. Thank you!")
            break
 
        else:
            print("Invalid option, please try again.")
 
 
# Run the program
if __name__ == "__main__":
    main()