import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import pearsonr

class SequenceEvaluator:
    def __init__(self):
        self.noise_loss_tracker = []

    def evaluate(self, actual_sequences, predicted_sequences, sequence_names, output_directory):
        noise_loss = 0.0
        seq_losses = []
        seq_maes = []
        seq_pccs = []
        results = []

        num_samples = min(len(actual_sequences), len(predicted_sequences))

        for i in range(num_samples):
            actual_seq = actual_sequences[i]
            predicted_seq = predicted_sequences[i]
            
            # Compare sequences of potentially different lengths
            seq_length = min(len(actual_seq), len(predicted_seq))
            mse = mean_squared_error(actual_seq[:seq_length], predicted_seq[:seq_length])
            mae = mean_absolute_error(actual_seq[:seq_length], predicted_seq[:seq_length])
            pcc, _ = pearsonr(actual_seq[:seq_length], predicted_seq[:seq_length])

            seq_losses.append(mse)
            seq_maes.append(mae)
            seq_pccs.append(pcc)
            noise_loss += mse

            results.append([sequence_names[i], mse, mae, pcc])

        noise_loss /= num_samples
        self.noise_loss_tracker.append(noise_loss)
        
        # Save results to CSV
        results_df = pd.DataFrame(results, columns=["Sequence Name", "MSE", "MAE", "PCC"])
        results_df.to_csv(output_directory + "evaluation_results.csv", index=False)

        return predicted_sequences

    def evaluate_self_similarity(self, sequences, sequence_names, dataset_name, output_directory):
        seq_losses = []
        seq_maes = []
        seq_pccs = []
        results = []

        num_samples = len(sequences)

        for i in range(num_samples):
            for j in range(i + 1, num_samples):
                seq1 = sequences[i]
                seq2 = sequences[j]
                
                seq_length = min(len(seq1), len(seq2))
                mse = mean_squared_error(seq1[:seq_length], seq2[:seq_length])
                mae = mean_absolute_error(seq1[:seq_length], seq2[:seq_length])
                pcc, _ = pearsonr(seq1[:seq_length], seq2[:seq_length])

                seq_losses.append(mse)
                seq_maes.append(mae)
                seq_pccs.append(pcc)

                results.append([f"Pair {i}-{j}", mse, mae, pcc])

        # Save results to CSV
        results_df = pd.DataFrame(results, columns=["Pair", "MSE", "MAE", "PCC"])
        results_df.to_csv(output_directory + f"self_similarity_{dataset_name}.csv", index=False)

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
predicted_file_path = "vae_probability/decode_data/TR/KNEE_TR_Bulk1.csv"
actual_file_path = "vae_probability/decode_data/TR/KNEE_TR_Bulk1.csv"
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

# Evaluate the sequences against each other
print("Evaluating predicted sequences against actual sequences:")
pred_sequences = evaluator.evaluate(actual_sequences, predicted_sequences, actual_sequence_names, output_directory)

# Evaluate the self-similarity within the actual sequences
print("\nEvaluating self-similarity within actual sequences:")
evaluator.evaluate_self_similarity(actual_sequences, actual_sequence_names, "Actual_Data", output_directory)

# Evaluate the self-similarity within the predicted sequences
print("\nEvaluating self-similarity within predicted sequences:")
evaluator.evaluate_self_similarity(predicted_sequences, pred_sequence_names, "Predicted_Data", output_directory)

# Save evaluation results
save_evaluation_results(pred_sequences, actual_sequences, output_directory)
