import pandas as pd
from sklearn.preprocessing import StandardScaler
import ast

# Load your original dataset
original_data = pd.read_csv('data/75609.csv')

# Load your encoded dataset
encoded_data = pd.read_csv('decoded_data/removed_padding.csv')

# Merge the original and encoded datasets based on 'PatientID' and 'BodyPart'
merged_data = pd.merge(encoded_data, original_data[['PatientID', 'BodyPart', 'Sequence', 'duration']], on=['PatientID', 'BodyPart'])

# Fit the StandardScaler on the 'duration' column
scaler = StandardScaler()
scaler.fit(original_data[['duration']])

# Reverse the standardization of the 'duration' column
merged_data[['duration']] = scaler.inverse_transform(merged_data[['duration']])

# Convert one-hot encoded sequences back to original sequences
decoded_sequences = []
for _, row in merged_data.iterrows():
    sequence = [col.split('_')[1] for col in merged_data.columns if row[col] == 1]
    decoded_sequences.append(sequence)

# Add the decoded sequences to the merged DataFrame
merged_data['decoded_sequences'] = decoded_sequences

# Group by 'PatientID' and 'BodyPart', aggregate the sequences and durations
grouped_data = merged_data.groupby(['PatientID', 'BodyPart']).agg({
    'decoded_sequences': lambda x: [ast.literal_eval(seq) for seq in x],
    'duration': lambda x: x.tolist()
}).reset_index()

# Format the 'decoded_sequences' column
grouped_data['decoded_sequences'] = grouped_data['decoded_sequences'].apply(lambda x: ', '.join(map(str, x)))

# Save the decoded data back to a CSV file
grouped_data.to_csv('decoded_original_data.csv', index=False)

print("Data decoding and processing successful!")
