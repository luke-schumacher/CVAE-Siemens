import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv('coded_data/decoded_sequences.csv')

# Filter rows where 'Sequence' contains 'SiemensSeq'
filtered_data = data[data['Sequence'].str.contains('SiemensSeq')]

# One-Hot Encoding
# Binary columns for each unique value in the 'Sequence' column
one_hot_encoded = pd.get_dummies(filtered_data, columns=['Sequence'], prefix='Seq')

# Extract 'duration' for standardization
duration_values = one_hot_encoded[['duration']].values

# Standardization
scaler = StandardScaler()
duration_values_standardized = scaler.fit_transform(duration_values)

# Replace 'duration' values with standardized values
one_hot_encoded['duration'] = duration_values_standardized

# Replace True and False with 1 and 0
one_hot_encoded.replace({True: 1, False: 0}, inplace=True)

# Inverse transform for each unique 'Sequence' value
for col in one_hot_encoded.filter(like='Seq_').columns:
    mask = one_hot_encoded[col] == 1
    one_hot_encoded.loc[mask, 'duration'] = scaler.inverse_transform(one_hot_encoded.loc[mask, ['duration']]) # type: ignore

# Round to a whole number
one_hot_encoded['duration'] = one_hot_encoded['duration'].round().astype(int)

# Export the modified data to a new CSV file
output_file_path = 'fully_decoded.csv'  # Replace with the desired path for the new CSV file
one_hot_encoded.to_csv(output_file_path, index=False)

print(f"\nModified data exported to: {output_file_path}")
