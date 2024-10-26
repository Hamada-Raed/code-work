import pandas as pd
import numpy as np

def calculate_grades(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        # Check for non-numeric data in student_number and quiz columns
        if not pd.to_numeric(df['student_number'], errors='coerce').notnull().all() or \
           not df[['quiz_1', 'quiz_2', 'quiz_3']].apply(pd.to_numeric, errors='coerce').notnull().all().all():
            return "Error: Non-numeric data found in student_number or quiz columns. Please modify the file."

        # Calculate the best grades (remove the lowest quiz score)
        df['best_grades'] = df[['quiz_1', 'quiz_2', 'quiz_3']].apply(lambda row: sum(sorted(row)[1:]), axis=1)

        # Adjust the total to be out of 15%
        df['total'] = (df['best_grades'] / 2) * 0.15

        # Save the updated DataFrame to a new CSV file
        df.to_csv(output_file, index=False)

        return f"Grades calculated and saved to {output_file}"

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
input_file = "grades.csv"
output_file = "new_grades.csv"
result = calculate_grades(input_file, output_file)
print(result)