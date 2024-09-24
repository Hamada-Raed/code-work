import tkinter as tk 
from tkinter import messagebox 



class Apartment:
    """
        Reoresents an apartment with details about the tenant and rent payments 
        
        Attributes 
            number: The apartment number. 
            tenant_name: The name of tenant occupting the apartment. 
            rent_amount: The amount of rent that the renant is required to pay. 
            payments: A dictionary tracking the payment status for each month. 
    """
    def __init__(self, number, tenant_name, rent_amount): 
        """
            Initialize the Apartment class with an apartment number, tenant's name, and rent amount
            
        """
        self.number = number
        self.tenant_name = tenant_name 
        self.rent_amount = rent_amount
        self.payments = {} 
        
    def make_payment(self, month, amount):
        """
        Records the payment made by the renant for a specific month.
            Args: 
                month: The month for which the payment is being made. 
                amount: The amount of rent paid by the renant. 
        
        """
        if amount >= self.rent_amount:
            self.payments[month] = "Paid"
        elif amount > 0:
            self.payments[month] = f"Partial payment: {amount}"
        else: 
            self.payments[month] = "Unpaid"
            
    def get_payment_status(self, month): 
        """
        Retrieves the payment status of the renant for a specific month. 
            Args: 
                month: The month for which the payment status is being queried. 
                
            Return: 
                str: The payment status for the specified month. Defaults to "Unpaid" if no record is found. 
        """
        return self.payments.get(month, "Unpaid")
        
    def send_reminder(self, month):

        """
            Send a reminder to the tenant if payment for a specific month is unpaid. 
            
            Args: 
                month: The month for which a payment reminder should be sent. 
        
        """
        status = self.get_payment_status(month)
        if status == "Unpaid":
            print(f"Reminder: Tenant {self.tenant_name} in Apartment {self.number} has not paid for {month}")
        
    def generate_monthly_report(self): 
        """
            Generates a report of the tanent's payment status for each month. 
            
            Return: 
                str: A formated string report of the payment status for each month
        
        """
        report = f"Apartment {self.number}, Tenant {self.tenant_name}\n"
        report += "Monthly payment status:\n"
        for month, status in self.payments.items():
            report += f"{month}: {status}\n"
        return report
    
    def reset_payment_status(self): 
        """
        Resets the payment status for all months, typically used when starting a new month
        """
        self.payments = {} # Clear all payment statuses for a new month 
        
# Create the apartments with tenant names amd rent amount          
apartments = [
    Apartment(1, "Tenant 1", 800),
    Apartment(2, "Tenant 2", 700),
    Apartment(3, "Tenant 3", 900),
    Apartment(4, "Tenant 4", 450),
    Apartment(5, "Tenant 5", 950),
    Apartment(6, "Tenant 6", 800),
]


def make_payment ():
    try: 
        apt_number = int(entry_apartment_number.get())
        month = entry_month.get()
        amount = float(entry_amount.get())
        
        for apartment in apartments: 
            if apartment.number == apt_number:
                message = apartment.make_payment(month, amount)
                messagebox.showinfo("Payment Status", message)
                return messagebox.showwarning("Error", "Apartment Not Found")
    except ValueError: 
        messagebox.showerror("Input Error", "Please enter valid data.")
        
def send_remider():
    try: 
        apt_number = int(entry_apartment_number.get())
        month = entry_month.get()
        for apartment in apartments: 
            if apartment.number == apt_number: 
                message = apartment.send_reminder(month)
                messagebox.showinfo("Reminder", message)
                return messagebox.showwarning("Error", "Apartment not found")
    except ValueError: 
        messagebox.showerror("Input Error", "Please enter valid data")
        
def generate_report(): 
    try: 
        apt_number = int(entry_apartment_number.get())
        for apartment in apartments: 
            if apartment.number == apt_number: 
                report = apartment.generate_monthly_report()
                messagebox.showinfo("Montly Report", report)
                return messagebox.showwarning("Error", "Apartment not found")
    except ValueError: 
        messagebox.showerror("Input Error", " Please enter valid data.")
                    
root = tk.Tk()
root.title("Apartment Payment System")

tk.Label(root, text="Apartment Number:").grid(row=0, column=0)
tk.Label(root, text="Month").grid(row=1, column=0)
tk.Label(root, text="Amount").grid(row=2, column=0)

entry_apartment_number = tk.Entry(root)
entry_month = tk.Entry(root)
entry_amount = tk.Entry(root)


entry_apartment_number.grid(row=0, column=1)
entry_month.grid(row=1, column=1)
entry_amount.grid(row=2, column=1)

tk.Button(root, text="Make Payment", command=make_payment).grid(row=3, column=0)
tk.Button(root, text="Send Reminder", command=send_remider).grid(row=3, column=1)
tk.Button(root, text="Generate Report", command=generate_report).grid(row=4, column=0, columnspan=2)

root.mainloop()