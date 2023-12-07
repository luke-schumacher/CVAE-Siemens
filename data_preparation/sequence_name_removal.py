import pandas as pd

def replace_column_names(csv_path, output_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Replace part of the column names and remove '\'
    new_columns = [col.replace('_%SiemensSeq%', 'Seq_').replace('\\', '') for col in df.columns]
    df.columns = new_columns

    # Write the modified DataFrame to a new CSV file
    df.to_csv(output_path, index=False)

# Example usage:
input_csv_path = 'encoded_data/182627/seq_&_duration_encoded.csv'
output_csv_path = 'encoded_data/182627/flawless_seq.csv'
replace_column_names(input_csv_path, output_csv_path)

