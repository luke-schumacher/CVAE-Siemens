import os
import pandas as pd

# Paths to the three CSV files
file_paths = [
    'model_results/175608/compiled_175608_.csv',
    'model_results/202531/compiled_202531_.csv',
    'model_results/182627/compiled_182627_.csv',
]

# List to store individual DataFrames
dfs = []

# Loop through each CSV file in the list of file paths
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Combine the DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined DataFrame to a new CSV file
output_file = 'gen_model_results.csv'
combined_df.to_csv(output_file, index=False)

# Displaying the combined DataFrame
print(combined_df)
