import pandas as pd

# Load the CSV file
df = pd.read_csv('data/176625_Brain.csv')

# Initialize a dictionary to store sequences for each patient
sequences_dict = {}

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    patient_id = row['PatientID']
    sequence = row['Sequence']
    
    # If patient ID is not already in the dictionary, add it
    if patient_id not in sequences_dict:
        sequences_dict[patient_id] = []
    
    # Append sequence to the list of sequences for this patient
    sequences_dict[patient_id].append(sequence)

# Create a new dataframe with patient IDs as index and sequences as columns
new_df = pd.DataFrame.from_dict(sequences_dict, orient='index')

# Transpose the dataframe so that patients are columns
new_df = new_df.transpose()

# Rename columns to be numbered sequentially
new_df.columns = [f'Sequence_{i}' for i in range(1, len(new_df.columns) + 1)]

# Write the new dataframe to a CSV file
new_df.to_csv('encoded_data/Brain/176625_filtered_sequences.csv')
