import pandas as pd
import ast

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('encoded_data/176398/split_patientID_array.csv')

def pad_data(row, desired_sequence_length, desired_duration_length):
    sequences = ast.literal_eval(row['Sequences'])
    durations = ast.literal_eval(row['Durations'])

    # Check if sequences is a tuple, and convert each element to a list
    if isinstance(sequences, tuple):
        sequences = [list(seq) for seq in sequences]
    else:
        sequences = [list(sequences)]

    # Check if durations is a tuple, and convert each element to a list
    if isinstance(durations, tuple):
        durations = [list(dur) for dur in durations]
    else:
        durations = [list(durations)]

    print(f"\nProcessing PatientID: {row['PatientID']}")
    print(f"Original Sequences: {sequences}")
    print(f"Original Durations: {durations}")

    # Check if the length of sequences is greater than the desired length
    if len(sequences) > desired_sequence_length:
        print(f"Skipping PatientID {row['PatientID']} - Sequences length exceeds desired_sequence_length")
        return None  # Skip this row

    # Pad sequences with the specified dummy data
    sequences += [[0] * 66] * (desired_sequence_length - len(sequences))
    print(f"Padded Sequences for PatientID {row['PatientID']}: {sequences}")

    # Pad durations with the specified dummy data
    durations += [[-0.7464702259125702]] * (desired_duration_length - len(durations))
    print(f"Padded Durations for PatientID {row['PatientID']}: {durations}")

    # Ensure both 'Sequences' and 'Durations' have the same length
    min_length = min(len(sequences), len(durations))
    sequences = sequences[:min_length]
    durations = durations[:min_length]

    print(f"Final Sequences for PatientID {row['PatientID']}: {sequences}")
    print(f"Final Durations for PatientID {row['PatientID']}: {durations}")

    return pd.Series({'Sequences': sequences, 'Durations': durations})

# Set your desired sequence and duration lengths
desired_sequence_length = 25
desired_duration_length = 25

# Apply the pad_data function to each row of the DataFrame
df[['Sequences', 'Durations']] = df.apply(lambda row: pad_data(row, desired_sequence_length, desired_duration_length), axis=1) # type: ignore

# Drop rows where pad_data returned None (sequences longer than desired)
df = df.dropna()

# Save the modified DataFrame back to a CSV file
df.to_csv('encoded_data/176398/prepared_data_176398.csv', index=False)
print("\nProcessing completed. Check padded_data.csv for the modified data.")
