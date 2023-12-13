import pandas as pd

# Read input data from a CSV file
input_file = 'model_results/175608/compiled_175608.csv'
df = pd.read_csv(input_file)

# Adding the 'SequenceCount' column
df['SequenceCount'] = df.groupby('BodyGroup').cumcount() + 1

# Reordering the columns as per your request
df = df[['SequenceCount', 'Sequences', 'SN', 'BodyGroup']]

# Write the result to a new CSV file
output_file = 'model_results/175608/compiled_175608_.csv'
df.to_csv(output_file, index=False)

# Displaying the result
print(df)
