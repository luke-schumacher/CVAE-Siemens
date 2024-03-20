import csv

# Read data from the CSV file
input_file_path = 'vae_probability/output_data/generated_samples_176015_Brain.csv'
output_file_path = 'vae_probability/output_data/generated_samples_176015_Brain.csv'

with open(input_file_path, 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)[1:]  # Exclude the first line containing the title

# Process the data
processed_data = []
for row in data:
    processed_row = []
    for item in row:
        # Remove '.0' from each element in the column
        items = item.split(', ')
        items = [i.replace('.0', '') for i in items]
        processed_row.append(', '.join(items))

    processed_data.append(processed_row)

# Write processed data to a new CSV file
with open(output_file_path, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(processed_data)

print(f"Processing complete. Output saved to {output_file_path}")
