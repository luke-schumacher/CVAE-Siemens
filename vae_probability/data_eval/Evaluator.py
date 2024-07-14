import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error

class SequenceEvaluator:
    def __init__(self):
        self.noise_loss_tracker = []

    def evaluate(self, actual_sequences, predicted_sequences, sequence_names):
        noise_loss = 0.0
        seq_losses = []

        num_samples = min(len(actual_sequences), len(predicted_sequences))

        for i in range(num_samples):
            actual_seq = actual_sequences[i]
            predicted_seq = predicted_sequences[i]
            
            # Compare sequences of potentially different lengths
            seq_length = min(len(actual_seq), len(predicted_seq))
            seq_loss = mean_squared_error(actual_seq[:seq_length], predicted_seq[:seq_length])
            seq_losses.append(seq_loss)
            noise_loss += seq_loss

        noise_loss /= num_samples
        self.noise_loss_tracker.append(noise_loss)
        
        # Print results with sequence names
        print(f"Noise Loss: {noise_loss}")
        print("Sequence Losses:")
        for seq_name, loss in zip(sequence_names, seq_losses):
            print(f"{seq_name}: {loss}")

        return predicted_sequences

def load_and_encode_sequences(file_path):
    df = pd.read_csv(file_path, header=0)
    label_encoder = LabelEncoder()

    for column in df.columns:
        df[column] = label_encoder.fit_transform(df[column].astype(str))

    return df.values.tolist(), df.columns.tolist()

def save_evaluation_results(pred_sequences, actual_sequences, output_directory):
    pred_df = pd.DataFrame(pred_sequences)
    actual_df = pd.DataFrame(actual_sequences)
    
    pred_df.to_csv(output_directory + "predicted_sequences.csv", index=False)
    actual_df.to_csv(output_directory + "actual_sequences.csv", index=False)

    print(f"Evaluation results saved to {output_directory}")

# File paths
predicted_file_path = "vae_probability/decode_data/176625/Brain_176625_7.csv"
actual_file_path = "vae_probability/decode_data/176625/ORIGINAL_176625.csv"
output_directory = "vae_probability/data_eval/"

# Load sequences
predicted_sequences, pred_sequence_names = load_and_encode_sequences(predicted_file_path)
actual_sequences, actual_sequence_names = load_and_encode_sequences(actual_file_path)

# Ensure there are no discrepancies in length between actual and predicted sequences
if len(predicted_sequences) != len(actual_sequences):
    min_length = min(len(predicted_sequences), len(actual_sequences))
    predicted_sequences = predicted_sequences[:min_length]
    actual_sequences = actual_sequences[:min_length]

# Create an evaluator instance
evaluator = SequenceEvaluator()

# Evaluate the sequences
pred_sequences = evaluator.evaluate(actual_sequences, predicted_sequences, actual_sequence_names)

# Save evaluation results
save_evaluation_results(pred_sequences, actual_sequences, output_directory)
