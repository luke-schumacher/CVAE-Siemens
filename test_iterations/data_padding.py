import pandas as pd
import ast

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data/split_patientID_array.csv')

# Function to pad sequences and durations
def pad_data(row, desired_sequence_length, desired_duration_length):
    sequences = ast.literal_eval(row['Sequences'])
    durations = ast.literal_eval(row['Durations'])

    print(f"\nProcessing PatientID: {row['PatientID']}")

    # Check if the length of sequences is greater than the desired length
    if len(sequences) > desired_sequence_length:
        print(f"Skipping PatientID {row['PatientID']} - Sequences length exceeds desired_sequence_length")
        return None  # Skip this row

    # Pad sequences with the specified dummy data
    sequences += [[0] * 25] * (desired_sequence_length - len(sequences))
    print(f"Padded Sequences for PatientID {row['PatientID']}")

    # Pad durations with the specified dummy data
    durations += [-0.7464702259125702] * (desired_duration_length - len(durations))
    print(f"Padded Durations for PatientID {row['PatientID']}")

    # Add extra sequences for each padded duration
    sequences += [[0] * 25] * (desired_duration_length - len(durations))
    print(f"Added Extra Sequences for Padded Durations for PatientID {row['PatientID']}")

    return pd.Series({'Sequences': str(sequences), 'Durations': durations})

# Set your desired sequence and duration lengths
desired_sequence_length = 50
desired_duration_length = 50

# Apply the pad_data function to each row of the DataFrame
df[['Sequences', 'Durations']] = df.apply(lambda row: pad_data(row, desired_sequence_length, desired_duration_length), axis=1) # type: ignore

# Drop rows where pad_data returned None (sequences longer than desired)
df = df.dropna()

# Save the modified DataFrame back to a CSV file
df.to_csv('padded_data.csv', index=False)
print("\nProcessing completed. Check padded_data.csv for the modified data.")
