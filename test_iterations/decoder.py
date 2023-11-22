import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the split data
split_data = pd.read_csv('encoded_data/split_patientID_array.csv')

def parse_array(arr_string):
    # Replace ellipses with a placeholder value
    arr_string = arr_string.replace('...', '0.0')  # You can change '0.0' to any suitable placeholder
    return [float(val.strip()) if '.' in val else int(val.strip()) for val in arr_string[1:-1].split(',')]

# Apply the function to 'Array of sequence steps and duration' column
split_data['Array'] = split_data['Array of sequence steps and duration'].apply(parse_array)

# Load the encoded data
encoded_data = pd.read_csv('encoded_data/padded_data.csv')

# Reverse the one-hot encoding
sequence_columns = [col for col in encoded_data.columns if col.startswith('Seq_')]
encoded_data['Sequence'] = encoded_data[sequence_columns].idxmax(axis=1).str.replace('Seq_', '')

# Extract 'duration' column
duration_data = encoded_data[['duration']]

# Initialize the scaler and fit it on the 'duration' data
scaler = StandardScaler()
scaler.fit(duration_data)

# Inverse transform the 'duration' column to get it back to the original scale
encoded_data[['duration']] = scaler.inverse_transform(duration_data)

# Merge the two dataframes on 'PatientID' and 'Sequence'
merged_data = pd.merge(split_data, encoded_data[['PatientID', 'Sequence', 'duration']], on='PatientID')

# Keep only relevant columns
final_data = merged_data[['PatientID', 'Label', 'Sequence', 'duration']]

# Display the reverted data
print("Reverted Data:")
print(final_data.head())

# Save the reverted data to a CSV file
final_data.to_csv('reverted_data.csv', index=False)
