import pandas as pd
from textblob import TextBlob
import os

def clean_file(input_f, output_f):
    """
    Cleans the CSV data by removing unnecessary spaces and correcting misspelled words.
    """
    # Check if the file exists
    if not os.path.isfile(input_f):
        raise FileNotFoundError(f"The file {input_f} does not exist.")

    # Read the CSV file
    try:
        df = pd.read_csv(input_f)
    except Exception as e:
        raise Exception(f"Error reading the CSV file: {e}")


    # Define a function to correct misspelled words
    def clean_cell(cell):
        cell = str(cell).strip()
        #correct the spelling for the entire cell.
        cleaned_cell = str(TextBlob(cell).correct())
        return cleaned_cell

    # Apply the spell-checking function to each cell
    cleaned_df = df.applymap(clean_cell)
    # Save the cleaned dataframe without the index
    cleaned_df.to_csv(output_f, index=False)

# Example usage
try:
    input_csv = 'input_doc.csv'
    output_csv= 'output_doc.csv'
    clean_file(input_csv,output_csv)
except Exception as e:
    print(f"An error occurred: {e}")
