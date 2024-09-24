import pandas as pd

def calculate_payment(file_path): 
    try:
        df = pd.read_excel(file_path)  # Load the Excel sheet
        df.columns = df.columns.str.strip().str.lower()  # Normalize column names
        
        if "programmer" in df.columns and "hours" in df.columns:  # Use lower case for comparison
            df['total_payment'] = df['hours'] * 8  # Calculate total payment
            return df[["programmer", "hours", "total_payment"]]
        else: 
            print("Error: The file must contain 'Programmer' and 'Hours' columns.")
    except FileNotFoundError:
        print('Error: File not found. Please provide a valid file path.')
        return None

file_path = "/Users/Hamada/Desktop/hours_working.xlsx"

result = calculate_payment(file_path)

if result is not None:
    print(result)
