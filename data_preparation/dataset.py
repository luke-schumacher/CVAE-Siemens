import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv('data/75609.csv')

# Verification
print("Original Data:")
print(data.head())

# Filter rows where 'Sequence' contains 'SiemensSeq'
filtered_data = data[data['Sequence'].str.contains('SiemensSeq')]

print("\nFiltered Data (Containing 'SiemensSeq' in 'Sequence' column):")
print(filtered_data.head())

# One-Hot Encoding
# Binary columns for each unique value in the 'Sequence' column
one_hot_encoded = pd.get_dummies(filtered_data, columns=['Sequence'], prefix='Seq')

# Standardisation
scaler = StandardScaler()
one_hot_encoded[['duration']] = scaler.fit_transform(one_hot_encoded[['duration']])

# Replace True and False with 1 and 0
one_hot_encoded.replace({True: 1, False: 0}, inplace=True)

print("\nOne-Hot Encoded and Standardized Data:")
print(one_hot_encoded.head())

one_hot_encoded.to_csv('seq_&_duration_encoded_data.csv', index=False)

print("Data encoding and processing successful!")
