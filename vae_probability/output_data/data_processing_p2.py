import csv

# Read sequences from CSV file
sequences = []
with open('vae_probability/output_data/generated_samples_176625_Brain.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Remove initial "[[" and trailing "]]"
        modified_row = row[0][2:-2]
        sequences.append([modified_row])

# Write modified sequences to a new CSV file
with open('vae_probability/output_data/generated_samples_176625_Brain.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sequences)


