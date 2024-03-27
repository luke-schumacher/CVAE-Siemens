import pandas as pd

# Read the CSV file, without considering any row as headers
df = pd.read_csv("vae_probability/decode_data/176625/Brain_176625_6.csv", header=None)

# Remove the first row (index 0)
df = df.iloc[1:]

# Add new headers manually from "Sequence_1" to "Sequence_28"
new_headers = [f"Sequence_{i}" for i in range(1, 29)]
df.columns = new_headers

# Iterate over each column
for column in df.columns:
    # Check if there's only one unique value in the column
    unique_values = df[column].dropna().unique()  # Drop NaN values
    if len(unique_values) == 1:
        # Drop the column if it contains only one unique value
        df.drop(column, axis=1, inplace=True)

# Pad down to 28 columns
current_columns = len(df.columns)
if current_columns < 28:
    # Add empty columns to pad up to 28 columns
    for i in range(28 - current_columns):
        df[f"Sequence_{current_columns + i + 1}"] = ""

# Save the modified CSV file, overwriting the original
df.to_csv("vae_probability/decode_data/176625/Brain_176625_7.csv", index=False)
