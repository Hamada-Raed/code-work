import datetime

class UnemploymentOffice:
    def __init__(self):
        # Dictionary to store unemployment benefit seekers
        # Key: seeker_id, Value: Dictionary with seeker details
        self.seekers = {}

    def add_seeker(self, seeker_id, name, age, application_date):
        """Add a new unemployment benefit seeker after scrutiny."""
        if seeker_id in self.seekers:
            raise ValueError("Seeker ID already exists.")
        if age >= 65:
            raise ValueError("Seeker is over the age limit for benefits.")
        
        self.seekers[seeker_id] = {
            'name': name,
            'age': age,
            'application_date': application_date,
            'status': 'active'
        }
        print(f"Seeker {name} added successfully.")

    def remove_seeker(self, seeker_id):
        """Remove a seeker from the list after they find employment or reach age 65."""
        if seeker_id not in self.seekers:
            raise KeyError("Seeker ID not found.")
        
        del self.seekers[seeker_id]
        print(f"Seeker ID {seeker_id} removed successfully.")

    def get_seekers(self, month=None, year=None):
        """Retrieve details of seekers for the current or specified month."""
        if month is None or year is None:
            today = datetime.date.today()
            month = today.month
            year = today.year
        
        seekers_in_month = {
            seeker_id: details for seeker_id, details in self.seekers.items()
            if datetime.datetime.strptime(details['application_date'], "%Y-%m-%d").month == month and
               datetime.datetime.strptime(details['application_date'], "%Y-%m-%d").year == year
        }
        
        return seekers_in_month

    def update_seeker_status(self, seeker_id, status):
        """Update the status of a seeker."""
        if seeker_id not in self.seekers:
            raise KeyError("Seeker ID not found.")
        
        self.seekers[seeker_id]['status'] = status
        print(f"Seeker ID {seeker_id} status updated to {status}.")

# Example usage
if __name__ == "__main__":
    office = UnemploymentOffice()
    
    # Adding seekers
    try:
        office.add_seeker("001", "John Doe", 30, "2023-09-15")
        office.add_seeker("002", "Jane Smith", 64, "2023-10-01")
    except ValueError as e:
        print(e)
    
    # Retrieving seekers for the current month
    try:
        current_month_seekers = office.get_seekers()
        print("Current month seekers:", current_month_seekers)
    except Exception as e:
        print(e)
    
    # Removing a seeker
    try:
        office.remove_seeker("001")
    except KeyError as e:
        print(e)
    
    # Updating seeker status
    try:
        office.update_seeker_status("002", "employed")
    except KeyError as e:
        print(e)