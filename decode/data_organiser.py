import pandas as pd

# Read the data from the CSV file
file_path = 'model_results/175608/brain_175608.csv'
df = pd.read_csv(file_path, header=None, names=['Sequences'])

# Replace "Seq_" with "%SiemensSeq%\"
df['Sequences'] = df['Sequences'].str.replace('Seq_', '%SiemensSeq%\\')

# Add 'SN' and 'BodyGroup' columns
df['SN'] = 175608
df['BodyGroup'] = 'Brain'

# Save the modified dataframe to a new CSV file
output_file_path = 'model_results/175608/compiled_175608_brain.csv'
df.to_csv(output_file_path, index=False)

print("Transformation completed. Data saved to", output_file_path)
