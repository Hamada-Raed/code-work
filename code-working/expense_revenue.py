import pandas as pd 
import matplotlib.pyplot as plt


def analyze_financial_date(file_path): 
    data = pd.read_excel(file_path)
    
    
    print("Original Data:")
    print(data) 
    
    expenses = data[data['type'] == 'Expense']
    revenues = data[data['type'] == 'Revenue'] 
    
    
    total_expenses = expenses['amount'].sum()
    total_revenues = revenues['amount'].sum()
    
    balance = total_revenues - total_expenses
    
    expenses['category'] = expenses['description'].apply(lambda x:x.split()[0] if isinstance(x,str) else "Uncategorized")
    expenses_categories = expenses.groupby('category')['amount'].sum().reset_index() 
    
    
    print('\n Total Expenses', total_expenses)
    print('\n Total Revenues', total_revenues)
    print('\n Total Balance', balance) 
    print('\n Expenses by Category')
    print(expenses_categories) 
    
    plt.figure(figsize=(10, 5))

    plt.subplot(1,2,1)
    plt.bar(expenses_categories['category'], expenses_categories['amount'], color = 'red')
    plt.title('Expenses by Category') 
    plt.xlabel('Category')
    plt.xlabel('Amount')
    
    plt.subplot(1,2,1)
    plt.bar(["Revenues"], [total_revenues], color = 'green')
    plt.title('Total Revenues')
    plt.ylabel('Amount') 
    
    plt.tight_layout()
    plt.show()
    
    
if __name__ == "__main__": 
    file_path = '/Users/Hamada/Desktop/data.xlsx'
    analyze_financial_date(file_path)     