import ast
import csv

# Function to add single quotation marks to sequences
def add_quotes(sequence):
    if isinstance(sequence, list):
        return str(sequence)
    elif isinstance(sequence, str):
        try:
            # Use ast.literal_eval to safely convert the string representation of a list to a list
            sequence_list = ast.literal_eval(sequence)
            return str(sequence_list)
        except (SyntaxError, ValueError):
            # Handle the case where ast.literal_eval fails
            return sequence

# Input and output file paths
input_file_path = 'data/padded_data.csv'
output_file_path = 'string_converted.csv'

# Read data from CSV file
with open(input_file_path, 'r') as input_file:
    reader = csv.reader(input_file)
    data = [row for row in reader]

# Process each element in the data
processed_data = [[add_quotes(element) for element in row] for row in data]

# Write processed data to CSV file
with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(processed_data)

print(f"Processed data has been written to {output_file_path}")
