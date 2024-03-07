import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv('data/202531_knee.csv')

# Verification
print("Original Data:")
print(data.head())

# One-Hot Encoding
# Binary columns for each unique value in the 'SeqGroup' column
one_hot_encoded = pd.get_dummies(data, columns=['Sequence'], prefix='')

# Standardisation
scaler = StandardScaler()
one_hot_encoded[['duration']] = scaler.fit_transform(one_hot_encoded[['duration']])

# Replace True and False with 1 and 0
one_hot_encoded.replace({True: 1, False: 0}, inplace=True)

print("\nOne-Hot Encoded and Standardized Data:")
print(one_hot_encoded.head())

one_hot_encoded.to_csv('encoded_data/Knee/seq_&_duration_encoded.csv', index=False)

print("Data encoding and processing successful!")
