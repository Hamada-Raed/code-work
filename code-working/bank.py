import tkinter as tk 
from tkinter import messagebox 

bank_accounts = {
    "Bank A" : 1000, 
    "Bank B" : 2000, 
    "Bank C" : 1500, 
    "Bank D" : 500, 
}

def transfer_meney(): 
    bank = selected_bank.get() 
    amount = entry_amount.get() 
    
    if not amount.isdigit(): 
        return messagebox.showerror("Invalid Input", "Please enter a valid amount.")

    amount = int(amount)
    
    if amount > bank_accounts[bank]: 
        return messagebox.showerror("Insufficient Funds", f"Not enough funds in {bank}. Available: {bank_accounts[bank]}")
    
    else: 
        bank_accounts[bank] -= amount 
        messagebox.showinfo("Success", f"Transfer of {amount} from {bank} completed successfully.")
        update_balance() 
        
    
def update_balance(): 
    balance_text = ""
    for bank, balance in bank_accounts.items():
        balance_text += f"{bank}: {balance}\n"
        
    label_balance.config(text = balance_text)
    

root = tk.Tk()
root.title("Bank Transfer System")

selected_bank = tk.StringVa() 
selected_bank.set("Bank A")

label_back = tk.Label(root, text="Select Bank")
label_back.pack() 

label_amount = tk.Label(root, text="Enter Amount:")
label_amount.pack() 

entry_amount = tk.Entry(root) 
entry_amount.pack() 

button_transfer = tk.Button(root, text="Transfer", command= transfer_meney)
button_transfer.pack()
 
update_balance() 

root.mainloop()



