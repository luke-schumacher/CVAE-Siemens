import pandas as pd

def filter_and_save_csv(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Filter rows containing the word 'KNEE'
    df = df[df.apply(lambda row: 'KNEE' in ' '.join(map(str, row)), axis=1)]

    # Remove columns with the number 0 in the title
    df = df.loc[:, ~df.columns.str.contains('0')]

    # Save the filtered DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

# Replace 'input.csv' and 'output.csv' with your actual file names
input_file = '202531.csv'
output_file = '202531_knee.csv'
filter_and_save_csv(input_file, output_file)
