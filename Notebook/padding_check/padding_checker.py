import pandas as pd
import ast  # For parsing string representations of lists
import numpy as np

# Read the CSV file
df = pd.read_csv("Notebook/prepared_data_176015.csv")

# Function to count elements in a list (ignoring the specific values)
def count_elements(lst):
    return sum(1 for element in lst if element != 0)

# Count elements in the "Sequences" column
df['Sequences_Count'] = df['Sequences'].apply(lambda x: count_elements(ast.literal_eval(x)))

# Count elements in the "Durations" column
df['Durations_Count'] = df['Durations'].apply(lambda x: len(ast.literal_eval(x)))

# Add the shape of each line in the "Sequences" column
df['Sequences_Shape'] = df['Sequences'].apply(lambda x: np.array(ast.literal_eval(x)).shape)

# Save the updated DataFrame to a new CSV file
df.to_csv("output_file.csv", index=False)
