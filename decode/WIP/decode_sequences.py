import pandas as pd

# Define the sequence mapping
sequence_mapping = [
    "Seq_%SiemensSeq%\AALScout", "Seq_%SiemensSeq%\BEAT", "Seq_%SiemensSeq%\BEAT_FQ",
    "Seq_%SiemensSeq%\BEAT_map", "Seq_%SiemensSeq%\CV_nav", "Seq_%SiemensSeq%\dess",
    "Seq_%SiemensSeq%\ep2d_diff", "Seq_%SiemensSeq%\ep2d_fid", "Seq_%SiemensSeq%\fast_tse",
    "Seq_%SiemensSeq%\fl3d_ce", "Seq_%SiemensSeq%\fl3d_vibe", "Seq_%SiemensSeq%\gre",
    "Seq_%SiemensSeq%\gre_field_mapping", "Seq_%SiemensSeq%\haste", "Seq_%SiemensSeq%\qDWI",
    "Seq_%SiemensSeq%\resolve", "Seq_%SiemensSeq%\space", "Seq_%SiemensSeq%\svs_se",
    "Seq_%SiemensSeq%\svs_st", "Seq_%SiemensSeq%\tfl", "Seq_%SiemensSeq%\tfl_b1map",
    "Seq_%SiemensSeq%\tfl_cb", "Seq_%SiemensSeq%\trufi", "Seq_%SiemensSeq%\tse", "Seq_%SiemensSeq%\tse_dixon"
]

# Function to decode sequences
def decode_sequences(encoded_sequences):
    return [sequence_mapping[i] for i, val in enumerate(encoded_sequences) if val == 1]

# Read the data from CSV
data = pd.read_csv("decoded_data/removed_padding.csv")  # Replace with the actual file path

# Initialize an empty list to store the decoded results
decoded_results = []

# Iterate through each row in the dataframe
for index, row in data.iterrows():
    print(f"Processing row {index + 1}/{len(data)}") # type: ignore

    patient_id = row["PatientID"]
    body_part = row["BodyPart"]
    sequences = eval(row["Sequences"])  # Convert string representation of list to actual list
    durations = eval(row["Durations"])  # Convert string representation of list to actual list

    # Decode sequences and durations
    for seq, duration in zip(sequences, durations):
        decoded_sequences = decode_sequences(seq)

        # Append the result to the list
        decoded_results.append([patient_id, body_part, decoded_sequences, duration])

# Create a new dataframe from the decoded results
decoded_df = pd.DataFrame(decoded_results, columns=["PatientID", "BodyPart", "Sequence", "Duration"])

# Save the decoded dataframe to a new CSV file
decoded_df.to_csv("decoded_data/decoded_sequence.csv", index=False)

print("Decoding completed. Results saved to decoded_results.csv")
