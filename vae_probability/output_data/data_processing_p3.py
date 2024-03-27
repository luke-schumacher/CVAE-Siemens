# Input file path
input_file = "vae_probability/output_data/generated_samples_176625_Brain.csv"

# Output file path
output_file = "vae_probability/output_data/generated_samples_176625_Brain1.csv"

# Function to remove leading and trailing " from each element
def remove_quotes(element):
    return element.strip('"')

# Read the input CSV file
with open(input_file, 'r') as f:
    data = f.readlines()

# Remove quotes from each element and write to a new CSV file
with open(output_file, 'w') as f:
    for line in data:
        # Remove leading and trailing quotes from each element
        cleaned_line = ','.join(map(remove_quotes, line.strip().split(',')))
        f.write('[' + cleaned_line + ']\n')

print("CSV file successfully created.")
