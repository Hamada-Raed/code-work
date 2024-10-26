# import pandas as pd

# try:
#     # Load the dataset
#     df = pd.read_csv('my.csv')

#     # Convert 'Column1' to numeric, coercing errors to NaN
#     df['Column1'] = pd.to_numeric(df['Column1'], errors='coerce')

#     # Drop rows where 'Column1' is NaN (non-numeric values)
#     df = df.dropna(subset=['Column1'])

#     # Filter the DataFrame
#     filtered_df = df[df['Column1'] < 50]

#     # Calculate descriptive statistics
#     stats = filtered_df['Column1'].describe()

#     # Save the statistics to a .txt file
#     with open('column1_stats.txt', 'w') as f:
#         f.write(str(stats))

#     print("Descriptive statistics for 'Column1' (filtered < 50) saved to 'column1_stats.txt'")

# except FileNotFoundError:
#     print("Error: 'my.csv' file not found.")
# except KeyError:
#     print("Error: 'Column1' not found in the CSV file.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}") 


import pandas as pd

try:
    # Load the dataset
    df = pd.read_csv('my.csv')

    # Convert 'Column1' to numeric, coercing errors to NaN
    df['Column1'] = pd.to_numeric(df['Column1'], errors='coerce')

    # Drop rows where 'Column1' is NaN (non-numeric values)
    df = df.dropna(subset=['Column1'])

    # Filter the DataFrame (using <= as requested)
    filtered_df = df[df['Column1'] <= 50]

    # Calculate descriptive statistics
    stats = filtered_df['Column1'].describe()

    # Save the statistics to a .txt file
    with open('column1_stats.txt', 'w') as f:
        print(stats.to_string()) # print to file
    print("Descriptive statistics for 'Column1' (filtered <= 50) saved to 'column1_stats.txt'")

except FileNotFoundError:
    print("Error: 'my.csv' file not found.")
except KeyError:
    print("Error: 'Column1' not found in the CSV file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")