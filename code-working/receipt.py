
import csv 
from datetime import datetime 

def generate_receipt(sender_account, recipient_account, amount):
    
    """
    Generate a payment receipt for a money transfer. 
    
    Parameters: 
    sender_account(str): The account number of the sender
    recipient_account(str): The acount number of the recipient
    amount(float): The amount of money being transferred 
    
    Returns: 
    None: prints the receipt to the console and saves it to as CSV file.
    """ 
    transcation_id = f"TRX-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create the receipt text 
    receipt = f"""
    -----------------------------------
    
            PAYMENT RECEIPT
        
    -----------------------------------
    
    Transcation ID: {transcation_id}
    Date: {date_time} 
    Sender Account: {sender_account}
    Recipient Account: {recipient_account}
    Amount Transferred: ${amount: .2f}
    
    Thank you for your transaction!
    
    ------------------------------------    
    
    """
    
    print(receipt)
    
    save_receipt_to_cvs(transcation_id, date_time,sender_account, recipient_account, amount)
    
    
    def save_receipt_to_cvs(transcation_id, date_time,sender_account, recipient_account, amount):
        """
        Save the payment receipt details to a CSV file. 
        
        Parameters: 
        transcation_id(str): The unique ID for the transaction
        date_time(str): The date and time of the transaction
        sender_account(str): The account number of the sender 
        recipient_account(str): the account number of the recipient. 
        amount(float): The amount of money transferred 
        
        Returns: 
        None: Appends the receipt details to the CSV file 
        """
        with open('payment_receipt.cvs', mode='a', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow([transcation_id, date_time, sender_account, recipient_account, amount])
            
        print(f"Receipt saved as {transcation_id}")
        
if __name__ == '__main__':
    """
    Main functino to execute the bank payment receipt program. 
    
    Prompts the user sender's account number, recipient's account number, 
    and the amount to transfer. Calls the function to generate the receipt 
    """
    # Get user input for the transfet
    sender_account = input("Enter sender account number: ")
    recipient_account = input("Enter recipient account number: ")
    amount = float(input('Enter the amount to transfer: $'))
    
    # Generate the receipt 
    generate_receipt(sender_account, recipient_account, amount) 


