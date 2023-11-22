import pandas as pd

# Read the CSV file into a DataFrame
file_path = 'data/75609.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Count the number of unique PatientIDs
num_patients = df['PatientID'].nunique()

print(f'The number of unique patients is: {num_patients}')
