import pandas as pd

# Read the CSV file
df = pd.read_csv("vae_probability/decode_data/176015/Brain_176015_2.csv", header=None, names=['Sequence'])

# Initialize variables
column_data = {}
column_index = 1
current_column = []

# Iterate through each row in the DataFrame
for _, row in df.iterrows():
    if 'Seq' in row['Sequence']:
        if current_column:  # Add the current column if it's not empty
            column_data[f'Column_{column_index}'] = [', '.join(current_column)]
            column_index += 1
            current_column = []  # Reset the current column
        current_column.append(row['Sequence'])  # Start a new column with the current sequence
    elif 'END' in row['Sequence']:
        if current_column:  # Check if the current column is not empty
            column_data[f'Column_{column_index}'] = [', '.join(current_column)]
            column_index += 1
        current_column = []  # Reset the current column
    else:
        current_column.append(row['Sequence'])  # Add the sequence to the current column

# Add the last column if it's not empty
if current_column:
    column_data[f'Column_{column_index}'] = [', '.join(current_column)]

# Create a new DataFrame with the parsed sequences
new_df = pd.DataFrame(column_data)

# Save the new DataFrame to a CSV file
new_df.to_csv("vae_probability/decode_data/176015/Brain_176015_3.csv", index=False)

print("Parsed sequences saved to Brain_176015_3.csv")
