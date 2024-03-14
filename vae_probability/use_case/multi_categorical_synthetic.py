import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.compat.v2 as tf #type:ignore
import tensorflow_probability as tfp
from tensorflow.keras.layers import LSTM #type:ignore
import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.data_generator.sequence_with_categories import generate_data
from src.vae_model.multi_categorical_vae import build_vae_submodels
from src.vae_model.common_functions import build_vae_from_models
from ast import literal_eval

tf.enable_v2_behavior()

tfk = tf.keras
tfkl = tf.keras.layers
tfpl = tfp.layers
tfd = tfp.distributions


def prepare_sequence_data(file='Notebook_duration/prepared_data_176625_Brain.csv'):

    def add_1_at_end(sequence):
        # Check if the sequence contains only zeros
        if all(elem == 0 for elem in sequence):
            sequence.append(1)
        else:
            # Add 1 at the end
            sequence.append(0)
        return sequence

    def add_pseudo_state(sequences):
        for i in range(len(sequences)):
            sequences[i] = add_1_at_end(sequences[i])

        return sequences

    def read_data_from_csv(file):
        df = pd.read_csv(file)

        df['Sequences'] = df['Sequences'].apply(literal_eval)
        df['Sequences'] = df['Sequences'].apply(lambda x: add_pseudo_state(x))
        return df #make it so only the knee parts are trained and analysed for best results

    # Load data from CSV file
    df = read_data_from_csv(file)

    # Extract sequences
    sequences = np.array(df['Sequences'])

    return sequences

def post_process_sequences_and_export(samples_list, output_file='vae_probability/output_data/generated_samples_176625_Brain.csv'):
    # Create a list to store individual samples
    individual_samples = []

    for sample in samples_list:
        # Remove the 1 at the end from each sample
        processed_sample = sample[:, :-1]
        
        # Convert the processed sample to a list of lists
        list_of_lists_sample = processed_sample.tolist()

        # Wrap the list of lists sample in double brackets and append to the list
        individual_samples.extend([[list_of_lists_sample]])

    # Convert the list of individual samples to a DataFrame
    df = pd.DataFrame(individual_samples, columns=['Generated_Samples'])

    # Export the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Generated samples have been exported to {output_file}.")


def main(epochs=1):
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print(tf.test.gpu_device_name())

    if tf.test.gpu_device_name() != '/device:GPU:0':
        print('WARNING: GPU device not found.')
    else:
        print('SUCCESS: Found GPU: {}'.format(tf.test.gpu_device_name()))

    # Use the prepare_sequence_data function to get sequences
    sequences = prepare_sequence_data()

    # Input shape and VAE parameters
    input_shape = (25, 67)  # Update with your desired input shape
    encoded_size = 16  # Update with your desired encoded size
    base_depth = 16  # Update with your desired base depth

    encoder, decoder = build_vae_submodels(input_shape, encoded_size, base_depth)

    print(encoder.summary())
    print(decoder.summary())

    vae = build_vae_from_models(encoder, decoder)

    print(vae.summary())

    train_data, eval_data = generate_data(sequences=sequences, window_length=input_shape[0],
                                          num_features=input_shape[1], train_data_amount=2500,
                                          eval_data_amount=1000)

    _ = vae.fit(x=train_data,
                y=train_data,
                epochs=epochs,
                validation_data=(train_data, train_data))

    example_data_points = eval_data[:1]
    example_output_distributions = vae(example_data_points)

    # Samples
    num_samples = 25 #can be put to 25, mean deviation
    samples_list = []
    for n_sample in range(num_samples):
        sample = example_output_distributions.sample().numpy()
        samples_list.append(sample)

    # Post-process and export generated samples
    post_process_sequences_and_export(samples_list)


if __name__ == '__main__':
    main(epochs=25)
    
    #for one body group one model that creates nice synthetic data, after that we can move on to the next body groups
