import _datetime 


# Class representing a study space 
class StudySpace: 
    # Initialize the study space with an ID, price, and default availablitiy status 
    def __init__(self, space_id, price): 
        self.space_id = space_id 
        self.price = price
        self.is_occupied = False # Indicates if the space is currently occupied 
        self.reserved_by = None # User who reserved the space
        self.reserved_until = None # Time until the space is reserved 
        
    def check_availability(self): 
        # Check if the space is occupied 
        if self.is_occupied: 
            return False, f"Cannot reserve space {self.space_id}, it is aleady occupied."
        return True, f"Space {self.space_id} is available"
    
    def reserce_space(self, user, payment_amount, duration):
        # Attempt to reserve the space for a user 
        if self.is_occupied: 
            return False, f"Cannot reserve space {self.space_id}, it is aleady occupied."
        
        # Check if the payment amount matches the requireed price 
        if payment_amount != self.price: 
            return False, f"Payment amount {payment_amount}, does not match the price of the space {self.space_id}"
        # Reserve the space and set the resrvation details 
        self.is_occupied = True
        self.reserved_by = user 
        self.reserved_until = _datetime.datetime.now() + _datetime.timedelta(hours=duration)
        
        return True, f"Space {self.space_id} reserved successfully for {duration} hour(s) by {user}"
    
    def release_space(self): 
        # Release the space for the future reservations. 
        self.is_occupied = False
        self.reserved_by = None 
        self.reserved_until = None
        return f"Space {self.space_id} is now available for reservation"
    
# Class representing a user. 
class User: 
    def __init__(self, name, balance):
        # Initialize the user with a name and account balance.  
        self.name = name 
        self.balance = balance
        
    def make_payment(self, amount): 
        # Process the payment and update the user's balance
        if self.balance < amount:
            return False, f"Insufficient balance. You have {self.balance}, but need {amount}."
        self.balance -= amount
        return True, f"Payment of {amount} made successfully. Remaining balace: {self.balance}"
    
# Example of system functionality.  
if __name__ == "__main__" : 
    # Create a dictonary of study spaces with their respective costs. 
    spaces = {
        1 : StudySpace(1,50), # Space 1 costs 50 units
        2 : StudySpace(2,70), # Space 2 costs 70 units
        3 : StudySpace(3,30), # Space 3 costs 30 units
        4 : StudySpace(4,20), # Space 4 costs 20 units
        5 : StudySpace(5,90), # Space 5 costs 90 units
        
    }
    
    # Create a user with an initial balance 
    user = User("Hamada", 150)

    # User attempts to reserve space 1 
    space_id = 1 
    space = spaces[space_id] 
    
    # User attempts to make a payment for the reserved space 
    available, message = space.check_availability()
    
    if available: 
        # User attempts to make a payment for the reserved space 
        payment_successful, payment_message = user.make_payment(space.price)
        print(payment_message) 
        
        if payment_successful: 
            # Reserce the space if payment was successful 
            reversed, revervaion_message = space.reserce_space(user.name, space.price, 2)
            print(revervaion_message) 
    
    # Check availability again (should indicate the space is occupied)    
    available, message = space.check_availability() 
    print(message)
    
    # After some time, relase the space for future reservations 
    release_message = space.release_space()
    print(release_message)






