    import csv
    from datetime import datetime

    def save_receipt_to_csv(transaction_id, date_time, sender_account, recipient_account, amount):
        with open('payment_receipt.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([transaction_id, date_time, sender_account, recipient_account, amount])
        print(f"Receipt saved as {transaction_id}")

    def generate_receipt(sender_account, recipient_account, amount):
        transaction_id = f"TRX-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        receipt = f"""
        -----------------------------------
        
                PAYMENT RECEIPT
            
        -----------------------------------
        
        Transaction ID: {transaction_id}
        Date: {date_time}
        Sender Account: {sender_account}
        Recipient Account: {recipient_account}
        Amount Transferred: ${amount: .2f}
        
        Thank you for your transaction!
        
        ------------------------------------    
        
        """
        
        print(receipt)
        
        save_receipt_to_csv(transaction_id, date_time, sender_account, recipient_account, amount)

    if __name__ == '__main__':
        sender_account = input("Enter sender account number: ")
        recipient_account = input("Enter recipient account number: ")
        amount = float(input('Enter the amount to transfer: $'))
        
        generate_receipt(sender_account, recipient_account, amount)