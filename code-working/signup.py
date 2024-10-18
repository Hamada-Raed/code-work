# def validate_input(input_value, field_name, min_length):
#     if not input_value or len(input_value) < min_length:
#         print(f"Error: {field_name} must be at least {min_length} characters long and cannot be empty.")
#         return False
#     return True

# def validate_gender(gender):
#     if gender.lower() not in ["male", "female", "other"]:
#         print("Error: Gender must be 'Male', 'Female', or 'Other'.")
#         return False
#     return True

# def get_input(field_name, min_length):
#     while True:
#         value = input(f"Enter your {field_name}: ").strip()
#         if validate_input(value, field_name, min_length):
#             return value

# def get_gender():
#     while True:
#         gender = input("Enter your gender (Male/Female/Other): ").strip()
#         if validate_gender(gender):
#             return gender

# def signup_form():
#     print("Welcome to the Signup Form. Please fill in the following details.\n")
    
#     username = get_input("Username", 4)
#     first_name = get_input("First Name", 1)
#     last_name = get_input("Last Name", 1)
#     password = get_input("Password", 6)
#     gender = get_gender()
#     hobbies = get_input("Hobbies (comma-separated list)", 1)

#     print("\nSignup Successful!")
#     print(f"Entered Details:\nUsername: {username}\nFirst Name: {first_name}\nLast Name: {last_name}\nGender: {gender}\nHobbies: {hobbies}")

# if __name__ == "__main__":
#     signup_form() 


import os

class SignupForm:
    filename = "existing_users.txt"

    def __init__(self):
        self.username = ""
        self.first_name = ""
        self.last_name = ""
        self.gender = ""
        self.hobbies = ""
        self.password = ""
        self.existing_users = self.load_existing_users()
    
    def load_existing_users(self):
        """Load existing usernames from a file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [line.strip().lower() for line in file.readlines()]
        return []

    def save_username(self, username):
        """Save new username to the file."""
        with open(self.filename, "a") as file:
            file.write(username.strip().lower() + "\n")

    def validate_username(self, username):
        """Validate username"""
        if len(username) < 4:
            print("Error: Username must be at least 4 characters long.")
            return False
        if username.strip().lower() in self.existing_users:
            print("Error: Username already exists.")
            return False
        self.username = username
        return True

    def validate_name(self, name, field_name):
        """Validate name"""
        if not name.strip():
            print(f"Error: {field_name} cannot be empty.")
            return False
        return True

    def validate_gender(self, gender):
        """Validate gender"""
        if gender.lower() not in ["male", "female", "other"]:
            print("Error: Invalid gender. Please enter male, female, or other.")
            return False
        self.gender = gender
        return True

    def validate_hobbies(self, hobbies):
        """Validate hobbies"""
        if not hobbies.strip():
            print("Error: Hobbies cannot be empty.")
            return False
        self.hobbies = hobbies
        return True

    def validate_password(self, password):
        """Validate password"""
        if len(password) < 6:
            print("Error: Password must be at least 6 characters long.")
            return False
        self.password = password
        return True

    def signup(self):
        """Signup form"""
        username = input("Enter username: ")
        while not self.validate_username(username):
            username = input("Enter username: ")

        first_name = input("Enter first name: ")
        while not self.validate_name(first_name, "First name"):
            first_name = input("Enter first name: ")
        self.first_name = first_name

        last_name = input("Enter last name: ")
        while not self.validate_name(last_name, "Last name"):
            last_name = input("Enter last name: ")
        self.last_name = last_name

        gender = input("Enter gender (male/female/other): ")
        while not self.validate_gender(gender):
            gender = input("Enter gender (male/female/other): ")

        hobbies = input("Enter hobbies: ")
        while not self.validate_hobbies(hobbies):
            hobbies = input("Enter hobbies: ")

        password = input("Enter password: ")
        while not self.validate_password(password):
            password = input("Enter password: ")

        self.save_username(username.strip())
        print("\nSignup successful!")
        print(f"Username: {self.username}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Hobbies: {self.hobbies}")
        print(f"Password: {'*' * len(self.password)}")


if __name__ == "__main__":
    form = SignupForm()
    form.signup()
