import pandas as pd

# Load the CSV file
df = pd.read_csv('data/176625_Brain.csv')

# Filter out rows containing instances of "customer"
df = df[~df['Sequence'].str.contains('customer', case=False)]

# Initialize a dictionary to store sequences for each patient
sequences_dict = {}

# Iterate over each row in the filtered dataframe
for _, row in df.iterrows():
    patient_id = row['PatientID']
    sequence = row['Sequence']
    
    # Replace %SiemensSeq%\ with Seq_
    sequence = sequence.replace('%SiemensSeq%\\', 'Seq_')
    
    # If patient ID is not already in the dictionary, add it
    if patient_id not in sequences_dict:
        sequences_dict[patient_id] = []
    
    # Append sequence to the list of sequences for this patient
    sequences_dict[patient_id].append(sequence)

# Write the sequences to a CSV file
with open('encoded_data/Brain/176625_filtered_sequences.csv', 'w') as file:
    # Write column headers
    file.write(','.join([f'Sequence_{i+1}' for i in range(max(len(seqs) for seqs in sequences_dict.values()))]) + '\n')
    
    # Write sequences for each patient
    max_sequences = max(len(seqs) for seqs in sequences_dict.values())
    for i in range(max_sequences):
        sequences = [sequences_dict[patient_id][i] if i < len(sequences_dict[patient_id]) else '' for patient_id in sequences_dict]
        file.write(','.join([f'"{seq}"' for seq in sequences]) + '\n')
