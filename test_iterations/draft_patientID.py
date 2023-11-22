import pandas as pd
import numpy as np
import re

# Load your dataset
data = pd.read_csv('data/seq_&_duration_encoded.csv')

# Strip whitespaces from column names
data.columns = data.columns.str.strip()

# Ensure the column name is correct
unique_patients = data['PatientID'].unique()

# Initialize an empty list to store the final aggregated data
final_data = []

# Iterate through each unique patient
for patient in unique_patients:
    # Filter data for the specific patient
    patient_data = data[data['PatientID'] == patient]

    # Count the unique body parts
    bodypart_count = patient_data['BodyPart'].nunique()

    # Only proceed if there is exactly one unique body part
    if bodypart_count == 1:
        print(f"Processing PatientID: {patient} ")
        print(f"BodyPart count: {bodypart_count}")

        # Extract the encoded sequence columns
        sequence_columns = [col for col in data.columns if col.startswith('Seq_')]

        # Select the relevant columns including 'duration' and 'BodyPart'
        relevant_columns = ['BodyPart'] + sequence_columns + ['duration']

        # Extract the relevant columns and convert to numpy array
        patient_array = patient_data[sequence_columns + ['duration']].to_numpy()

        # Extract the label (BodyPart)
        label = patient_data['BodyPart'].iloc[0]

        # Set print options to remove whitespaces
        np.set_printoptions(floatmode='maxprec', suppress=True)

        # Aggregate the data for each patient into a single line
        aggregated_data = [patient, label, re.sub(r'(?<=\d)\.0', '', np.array2string(patient_array.flatten(), separator=','))]

        # Append to the final_data list
        final_data.append(aggregated_data)

        print(f"Aggregated Data:\n{aggregated_data}\n")
    else:
        print(f"Skipping PatientID: {patient} as it has more than one unique body part.\n")

# Create a DataFrame from the final_data list
final_df = pd.DataFrame(final_data, columns=['PatientID', 'Label', 'Array of sequence steps and duration'])

# Save the final DataFrame as a CSV file
final_df.to_csv('split_patientID_array.csv', index=False)

print("split_patientID_array.csv\n")
