import pandas as pd

# Load your dataset
data = pd.read_csv('data/seq_&_duration_encoded.csv')

# Strip whitespaces from column names
data.columns = data.columns.str.strip()

# Ensure the column name is correct and strip whitespaces
unique_patients = data['PatientID'].unique()

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
        patient_array = patient_data[relevant_columns].to_numpy()

        # Save the patient_array as a CSV file
        patient_csv_filename = f"patient_{patient}_data.csv"
        pd.DataFrame(patient_array, columns=relevant_columns).to_csv(patient_csv_filename, index=False)

        print(f"Patient Array:\n{patient_array}\n")
        print(f"Saved {patient_csv_filename}\n")
    else:
        print(f"Skipping PatientID: {patient} as it has more than one unique body part.\n")
