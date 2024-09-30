import datetime

cheques = []

def add_cheques():
    """
        Add new cheque to the list 
        
        prompts the user for cheques details such as cheque number, beneficiary name, amount, and date
        and appends the information to the "cheques" list. 
    """ 
    cheque_number = input('Enter cheque number: ')
    beneficiary = input("Enter beneficiary's name: ")
    amount = float(input("Enter cheque amount: "))
    date_str = input("Enter cheque date (yyyy-mm-dd): ")
    
    # Correcting the date parsing to use strptime instead of strftime
    cheque_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() 
    
    cheques.append({
        "Cheque Number": cheque_number, 
        "Beneficiary": beneficiary, 
        "Amount": amount, 
        "Date": cheque_date, 
    })
    
    print("Cheque added successfully! \n") 

def display_cheques(sort_by="Date"): 
    
    """
        Display all cheques sorted by a specified criterion
        
        args: 
            sort_by(str): The criterion by which to sort the cheques ( Date or amount)
        
        If no cheques are available, it informs the user that there are no cheques to display.
    
    """
    sorted_cheques = sorted(cheques, key=lambda x: x[sort_by])
    
    if len(sorted_cheques) == 0: 
        print("No cheques to display.")
    else: 
        for cheque in sorted_cheques: 
            # Use single quotes for keys inside the f-string
            print(f"Cheque Number: {cheque['Cheque Number']}, Beneficiary: {cheque['Beneficiary']}, Amount: {cheque['Amount']}, Date: {cheque['Date']}")

def search_cheque():
    """
        Search for a cheques by cheque number or beneficiary name. 
        
        Prompts the user to choose a search type (1 for cheque number or 2 for beneficiary name)
        and display the found cheques or notifies the user for no cheque is found. 
    """
    search_type = input('Choose search type (1: by cheque number, 2: by beneficiary name): ')
    
    if search_type == "1": 
        cheque_number = input("Enter cheque number: ")
        found_cheque = next((cheque for cheque in cheques if cheque["Cheque Number"] == cheque_number), None)
        
    elif search_type == "2": 
        beneficiary = input("Enter beneficiary name: ")
        found_cheque = next((cheque for cheque in cheques if cheque['Beneficiary'] == beneficiary), None)
        
    else: 
        print("Invalid option.")
        return 
    
    if found_cheque: 
        print(f"Cheque found: {found_cheque}")
    else: 
        print("Cheque not found") 

def cheque_management_system(): 
    """
        Run the cheque managment system in a loop untill the user chooses to exit. 
        
        Display a menu for the user to add cheques, display cheques, search for a cheques, or exit the system
    
    """
    while True: 
        print('\nCheque Management System')
        print('1. Add a new cheque')
        print('2. Display cheques')
        print('3. Search for a cheque')
        print('4. Exit') 
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1": 
            add_cheques()
        
        elif choice == "2": 
            sort_option = input("Sort cheques by (1: date, 2: amount): ")
            if sort_option == "1":
                display_cheques(sort_by="Date")
            
            elif sort_option == "2":
                display_cheques(sort_by="Amount")
                
            else: 
                print("Invalid sorting option")
                
        elif choice == "3": 
            search_cheque()
            
        elif choice == "4": 
            print("Exiting the system.")
            break
        else: 
            print('Invalid option. Try again.')

cheque_management_system()
