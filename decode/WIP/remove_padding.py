import pandas as pd
import ast

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('encoded_data/padded_data.csv')

# Function to remove specific durations
def remove_specific_durations(row):
    durations = ast.literal_eval(row['Durations'])
    
    # Filter out specific durations (-0.7464702259125702)
    filtered_durations = [dur[0] for dur in durations if dur != [-0.7464702259125702]]

    return pd.Series({'Durations': filtered_durations})

# Function to remove empty sequences and sequences without '1'
def remove_empty_sequences(row):
    sequences_str = row['Sequences']

    # Convert the sequences string to a list
    sequences_list = ast.literal_eval(sequences_str)

    # Filter out empty sequences and keep only sequences with at least one '1'
    filtered_sequences_list = [seq for seq in sequences_list if seq and any(val == 1 for val in seq)]

    # If the filtered sequences list is empty, keep an empty list
    sequences_str_filtered = str(filtered_sequences_list) if filtered_sequences_list else '[]'

    return pd.Series({'Sequences': sequences_str_filtered})

# Apply the remove_empty_sequences function to each row of the DataFrame
df[['Sequences']] = df.apply(remove_empty_sequences, axis=1)

# Apply the remove_specific_durations function to each row of the DataFrame
df[['Durations']] = df.apply(remove_specific_durations, axis=1)

# Save the modified DataFrame back to a CSV file
df.to_csv('decoded_data/removed_padding.csv', index=False)
print("\nProcessing completed. Check original_data_filtered.csv for the modified data.")
