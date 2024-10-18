import datetime
import re
import logging
import json

# Set up basic configuration for logging errors to a file
logging.basicConfig(filename='unemployment_office.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class UnemploymentBenefitSeeker:
    def __init__(self, name, age, address, phone_number, registration_date, employment_status=False):
        """
        Initialize an UnemploymentBenefitSeeker object with name, age, address, phone number, and registration date.
        Ensures valid age, phone number format, and address.

        Args:
            name (str): Name of the seeker.
            age (int): Age of the seeker (must be a positive integer).
            address (str): Address of the seeker.
            phone_number (str): Phone number of the seeker (must be a valid format).
            registration_date (datetime.date): Date of registration.
            employment_status (bool): Employment status of the seeker (defaults to False).

        Raises:
            ValueError: If age is not a positive integer, phone number is invalid, or address is invalid.
        """
        # Validate age input
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        
        # Validate phone number format (e.g., must be 10 digits)
        if not re.match(r"^\d{10}$", phone_number):
            raise ValueError("Phone number must be a 10-digit number.")
        
        # Validate address (simple check for non-empty string)
        if not address or not isinstance(address, str) or len(address.strip()) == 0:
            raise ValueError("Address must be a valid non-empty string.")
        
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.registration_date = registration_date
        self.employment_status = employment_status  # Added employment status attribute

    def to_dict(self):
        """
        Convert the seeker object to a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the seeker object.
        """
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "phone_number": self.phone_number,
            "registration_date": str(self.registration_date),
            "employment_status": self.employment_status
        }

class UnemploymentOffice:
    def __init__(self):
        """Initialize an UnemploymentOffice object to manage unemployment benefit seekers."""
        self.seekers = {}
        self.load_seekers()  # Load seekers from persistent storage

    def add_seeker(self, name, age, address, phone_number):
        """
        Add a new unemployment benefit seeker with validated age, phone number, and address.

        Args:
            name (str): Name of the seeker.
            age (int): Age of the seeker (must be a positive integer).
            address (str): Address of the seeker (must be valid).
            phone_number (str): Phone number of the seeker (must be a valid format).

        Raises:
            ValueError: If the seeker is already registered, age is invalid, or phone number or address is invalid.
            TypeError: If any input type is incorrect.
        """
        try:
            if name in self.seekers:
                raise ValueError(f"Seeker '{name}' is already registered.")

            # Ensure age is a positive integer, phone number is valid, and address is non-empty
            if not isinstance(age, int) or age <= 0:
                raise ValueError("Age must be a positive integer.")
            if not re.match(r"^\d{10}$", phone_number):
                raise ValueError("Phone number must be a valid 10-digit number.")
            if not address or not isinstance(address, str) or len(address.strip()) == 0:
                raise ValueError("Address must be a valid non-empty string.")

            registration_date = datetime.date.today()
            self.seekers[name] = UnemploymentBenefitSeeker(name, age, address, phone_number, registration_date)
            print(f"Seeker '{name}' added successfully.")
            self.save_seekers()  # Save after adding

        except (ValueError, TypeError) as e:
            logging.error(f"Error adding seeker: {e}")
            print(f"Error: {e}")

    def get_seeker_details(self, name):
        """
        Retrieve the details of an unemployment benefit seeker.

        Args:
            name (str): Name of the seeker.

        Returns:
            UnemploymentBenefitSeeker: The details of the seeker if found.

        Raises:
            ValueError: If the seeker is not registered.
        """
        if name not in self.seekers:
            logging.error(f"Seeker '{name}' is not registered.")
            raise ValueError(f"Seeker '{name}' is not registered.")
        return self.seekers[name]

    def get_current_month_seekers(self):
        """
        Get the list of seekers who registered in the current month.

        Returns:
            list: A list of seekers registered this month.
        """
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        return [seeker for seeker in self.seekers.values() if seeker.registration_date.month == current_month and seeker.registration_date.year == current_year]

    def get_previous_month_seekers(self):
        """
        Get the list of seekers who registered in the previous month.

        Returns:
            list: A list of seekers registered last month.
        """
        current_date = datetime.date.today()
        first_of_current_month = current_date.replace(day=1)
        last_month_date = first_of_current_month - datetime.timedelta(days=1)
        last_month = last_month_date.month
        last_month_year = last_month_date.year

        return [seeker for seeker in self.seekers.values() if seeker.registration_date.month == last_month and seeker.registration_date.year == last_month_year]

    def remove_employed_seekers(self):
        """
        Remove all seekers who have found employment.
        """
        employed_seekers = [name for name, seeker in self.seekers.items() if seeker.employment_status]
        for name in employed_seekers:
            self.remove_seeker(name)
        print(f"Employed seekers removed: {employed_seekers}")

    def remove_seeker(self, name):
        """
        Remove an unemployment benefit seeker from the system if they are 65 or older or have found employment.

        Args:
            name (str): Name of the seeker to be removed.

        Raises:
            ValueError: If the seeker is not registered or is not eligible for removal.
        """
        if name not in self.seekers:
            logging.error(f"Seeker '{name}' is not registered.")
            raise ValueError(f"Seeker '{name}' is not registered.")
        
        seeker = self.seekers[name]
        
        # Check if seeker is 65 or older or employed before allowing removal
        if seeker.age < 65 and not seeker.employment_status:
            logging.error(f"Seeker '{name}' is younger than 65 and not employed, cannot be removed.")
            raise ValueError(f"Seeker '{name}' is younger than 65 and not employed, cannot be removed.")
        
        del self.seekers[name]
        print(f"Seeker '{name}' has been removed.")
        self.save_seekers()  # Save after removal

    def update_ages(self):
        """
        Update the age of all seekers at the start of a new year.
        """
        current_year = datetime.date.today().year
        for seeker in self.seekers.values():
            # Assuming age increment happens once a year
            seeker.age += 1
        print("All seekers' ages have been updated.")
        self.save_seekers()  # Save after updating ages

    def set_employment_status(self, name, status):
        """
        Update the employment status of a seeker.

        Args:
            name (str): Name of the seeker.
            status (bool): Employment status to be updated.

        Raises:
            ValueError: If the seeker is not registered.
        """
        if name not in self.seekers:
            logging.error(f"Seeker '{name}' is not registered.")
            raise ValueError(f"Seeker '{name}' is not registered.")
        
        self.seekers[name].employment_status = status
        self.save_seekers()  # Save after updating employment status
        print(f"Employment status for '{name}' has been updated to {'Employed' if status else 'Unemployed'}.")

    def remove_retired_seekers(self):
        """
        Remove seekers who have reached the retirement age of 65 using optimized list comprehension.
        """
        retired_seekers = [name for name, seeker in self.seekers.items() if seeker.age >= 65]
        for name in retired_seekers:
            self.remove_seeker(name)
        print(f"Retired seekers removed: {retired_seekers}")

    def save_seekers(self):
        """Save the seekers to a JSON file for persistent storage."""
        with open('seekers_data.json', 'w') as file:
            seekers_dict = {name: seeker.to_dict() for name, seeker in self.seekers.items()}
            json.dump(seekers_dict, file)

    def load_seekers(self):
        """Load seekers from a JSON file if it exists."""
        try:
            with open('seekers_data.json', 'r') as file:
                seekers_dict = json.load(file)
                for name, data in seekers_dict.items():
                    # Convert back to UnemploymentBenefitSeeker objects
                    registration_date = datetime.date.fromisoformat(data['registration_date'])
                    self.seekers[name] = UnemploymentBenefitSeeker(
                        name, data['age'], data['address'], data['phone_number'], registration_date, data['employment_status'])
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty dictionary
            self.seekers = {}

def main():
    office = UnemploymentOffice()

    # Add seekers with valid age, phone number, and address
    office.add_seeker("John Doe", 30, "123 Main St", "1234567890")
    office.add_seeker("Jane Doe", 64, "456 Elm St", "9876543210")

    # Get seekers registered in the current month
    current_month_seekers = office.get_current_month_seekers()
    print("Current month seekers:", [seeker.name for seeker in current_month_seekers])

    # Get seekers registered in the previous month
    previous_month_seekers = office.get_previous_month_seekers()
    print("Previous month seekers:", [seeker.name for seeker in previous_month_seekers])

    # Update age annually
    office.update_ages()

    # Mark employment status
    office.set_employment_status("John Doe", True)

    # Remove seekers who are 65 or older or have found employment
    office.remove_retired_seekers()
    office.remove_employed_seekers()


# Create an instance of the UnemploymentOffice class
office = UnemploymentOffice()

# Add a new seeker
office.add_seeker("John Doe", 30, "123 Main St", "1234567890")

# Get the details of a seeker
print(office.get_seeker_details("John Doe").__dict__)

# Remove a seeker
office.remove_seeker("John Doe")

# Get the list of seekers for the current month
print([seeker.name for seeker in office.get_current_month_seekers()])

# Get the list of seekers for the previous month
print([seeker.name for seeker in office.get_previous_month_seekers()])

# Remove seekers who have found employment
office.remove_employed_seekers(["John Doe", "Jane Doe"])

# Remove seekers who have reached the retirement age of 65
office.remove_retired_seekers()