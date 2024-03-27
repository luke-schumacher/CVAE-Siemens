import pandas as pd

# Read the CSV file
df = pd.read_csv("vae_probability/decode_data/176625/Brain_176625_5.csv", header=None, names=['Sequence'])

# Initialize variables
sequences_dict = {}
current_column = None
column_index = 1

# Iterate through each row in the DataFrame
for _, row in df.iterrows():
    if 'Seq' in row['Sequence']:
        if current_column is None:
            current_column = []
        current_column.append(row['Sequence'])
    elif 'END' in row['Sequence']:
        if current_column:  # Check if there are sequences in the current column
            sequences_dict[f'Sequence_{column_index}'] = current_column
            column_index += 1
            current_column = None  # Reset the current column

# If there's a remaining sequence, add it to the last column
if current_column:
    sequences_dict[f'Sequence_{column_index}'] = current_column

# Pad sequences to a length of 28
max_length = 28
for key, value in sequences_dict.items():
    value += [''] * (max_length - len(value))  # Fill empty rows with ""
    sequences_dict[key] = value

# Create a new DataFrame with the parsed sequences
new_df = pd.DataFrame(sequences_dict)

# Write the headers (first row) without modification
with open("vae_probability/decode_data/176625/Brain_176625_6.csv", "w") as f:
    f.write(",".join(new_df.columns) + "\n")

# Write the remaining data (excluding the headers) with each field enclosed within double quotes
new_df.to_csv("vae_probability/decode_data/176625/Brain_176625_6.csv", index=False, mode="a", header=False, quoting=1)

print("Parsed sequences saved to Brain_176625_6.csv")
