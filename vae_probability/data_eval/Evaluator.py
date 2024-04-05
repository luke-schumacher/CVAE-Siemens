import os
import pandas as pd
import numpy as np
import editdistance
from collections import Counter
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

# File paths
predicted_file_path = "vae_probability/decode_data/176625/Brain_176625_7.csv"
actual_file_path = "vae_probability/decode_data/176625/ORIGINAL_176625.csv"
output_directory = "vae_probability/data_eval/"

# Load predicted and actual sequences from CSV
predicted_df = pd.read_csv(predicted_file_path, header=None)
actual_df = pd.read_csv(actual_file_path, header=None)

# Replace NaN values with an empty string
predicted_df = predicted_df.fillna("")
actual_df = actual_df.fillna("")

# Extract unique sequence names
unique_labels = sorted(set(predicted_df.values.flatten()) | set(actual_df.values.flatten()))

# Construct confusion matrix
conf_matrix = confusion_matrix(actual_df.values.flatten(), predicted_df.values.flatten(), labels=unique_labels)

# Precision, Recall, F1-score
precision, recall, fscore, _ = precision_recall_fscore_support(actual_df.values.flatten(), predicted_df.values.flatten(), labels=unique_labels, average='macro')

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Save confusion matrix to CSV
conf_matrix_df = pd.DataFrame(conf_matrix, columns=unique_labels, index=unique_labels)
conf_matrix_df.to_csv(os.path.join(output_directory, "confusion_matrix.csv"))

# Print precision, recall, and F1-score
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", fscore)
