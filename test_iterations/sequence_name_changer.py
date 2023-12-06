import pandas as pd

def replace_values_in_column(csv_path, output_path, column_name):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Replace part of the values in the specified column and remove '\'
    df[column_name] = df[column_name].apply(lambda x: str(x).replace('%SiemensSeq%', 'Seq_').replace('\\', ''))

    # Write the modified DataFrame to a new CSV file
    df.to_csv(output_path, index=False)

# Example usage:
input_csv_path = 'data/176015.csv'
output_csv_path = 'updated_seq_names_176015.csv'
column_to_modify = 'Sequence'  
replace_values_in_column(input_csv_path, output_csv_path, column_to_modify)
