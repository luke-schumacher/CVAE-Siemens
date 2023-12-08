import pandas as pd
import glob

# List of file paths to combine
file_paths = [
    "model_results/182627/compiled_182627_brain.csv",
    "model_results/182627/compiled_182627_knee.csv",
    # Add more file paths as needed
]

# Initialize an empty dataframe
combined_df = pd.DataFrame()

# Iterate through the file paths and concatenate the dataframes
for file_path in file_paths:
    try:
        df = pd.read_csv(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    except FileNotFoundError:
        print(f"Warning: File not found at {file_path}")

# Save the combined dataframe to a new CSV file
combined_output_file_path = 'model_results/182627/compiled_182627.csv'
combined_df.to_csv(combined_output_file_path, index=False)

print(f"Combination completed. Data saved to {combined_output_file_path}")
