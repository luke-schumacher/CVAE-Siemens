import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with your actual file paths
file1_path = 'encoded_data/75609/unified_seq_75609.csv'
file2_path = 'encoded_data/176398/unified_seq_176398.csv'

# Read CSV files into Pandas DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Extract column names with 'Seq_' prefix
columns_file1 = [col for col in df1.columns if 'Seq_' in col]
columns_file2 = [col for col in df2.columns if 'Seq_' in col]

# Compare column names
differences = set(columns_file1) ^ set(columns_file2)

# Print the results
if differences:
    print("Columns with 'Seq_' prefix are different:")
    for diff in differences:
        print(diff)
else:
    print("Column names with 'Seq_' prefix are identical.")
