import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

file_path = "/Users/Hamada/Desktop/testDate.xlsx"

def analyze_expenses(file_path): 
    data = pd.read_excel(file_path) 
    
    data.columns = ['Date', 'Expenses']
    
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')
    
    plt.figure(figsize=(10,5))
    plt.plot(data['Date'], data['Expenses'], marker='o')
    plt.title('Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Expenses')  
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  
    
    max_expenses_date = data.loc[data['Expenses'].idxmax()]
    print(f'The day with the highest expenses is {max_expenses_date["Date"].strftime("%y-%m-%d")} with an amount of {max_expenses_date["Expenses"]}')  # Corrected to 'Expenses'
    
    mean_expenses = data['Expenses'].mean()
    std_dev_expenses = data['Expenses'].std()  
    
    print(f"Average Expenses: {mean_expenses:.2f}")  
    print(f"Standard Deviation of Expenses: {std_dev_expenses:.2f}")  

analyze_expenses(file_path)
