import pandas as pd

def count_unique_names(csv_file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the CSV file.")
        return

    # Extract the specified column and count unique names
    unique_names = df[column_name].nunique()

    # Print the result
    print(f"The column '{column_name}' contains {unique_names} unique names.")

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'output_file.csv'

# Replace 'group' with the actual column name you want to analyze
column_name = 'Group'

# Call the function
count_unique_names(csv_file_path, column_name)
