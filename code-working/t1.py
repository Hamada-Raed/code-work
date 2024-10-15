import pandas as pd
from textblob import TextBlob

def clean_file(input_file, output_file):
    df = pd.read_csv(input_file)

    def clean_cell(cell):
        # Convert cell to string and strip unnecessary spaces
        cell = str(cell).strip()
        # Correct spelling using TextBlob
        corrected_cell = str(TextBlob(cell).correct())
        return corrected_cell

    # Apply the cleaning function to each cell in the DataFrame
    cleaned_df = df.applymap(clean_cell)

    # Save the cleaned DataFrame to a new CSV file
    cleaned_df.to_csv(output_file, index=False)

# Define input and output file paths
input_file = 'input_doc.csv'
output_file = 'output_doc.csv'

# Call the function to clean the file
clean_file(input_file, output_file)

import pandas as pd
from textblob import TextBlob

def clean_file(input_f, output_f):
    df = pd.read_csv(input_f)

    def clean_cell( cell ):
        cell = str(cell).strip()
        cleaned_cell =  str(TextBlob(cell[0]).correct())+cell[1:]
        return cleaned_cell

    cleaned_df = df.applymap(clean_cell)

    cleaned_df.to_csv(output_f, index=True)

input = 'input_doc.csv'
output = 'output_doc.csv'
clean_file(input,output)