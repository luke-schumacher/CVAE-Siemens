import numpy as np

def generate_data(sequences,
                  window_length=10,
                  num_features=2,
                  train_data_amount=25000,
                  eval_data_amount=5000):
    """
    Generate data with random filling based on provided sequences.

    Parameters:
        sequences (numpy.ndarray): The sequence data to be filled into the arrays.
        window_length (int): Length of the sequence window.
        num_features (int): Number of features in each sequence.
        train_data_amount (int): Number of training data samples.
        eval_data_amount (int): Number of evaluation data samples.

    Returns:
        tuple: Tuple containing train_data and eval_data numpy arrays.
    """
    def fill_with_sequences(data, sequences):
        for i in range(data.shape[0]):
            sequence_idx = np.random.choice(range(sequences.shape[0]))
            data[i, :, :] = sequences[sequence_idx]

        return data

    train_data = np.zeros((train_data_amount, window_length, num_features))
    eval_data = np.zeros((eval_data_amount, window_length, num_features))

    train_data = fill_with_sequences(train_data, sequences)
    eval_data = fill_with_sequences(eval_data, sequences)

    np.random.shuffle(train_data)
    np.random.shuffle(eval_data)

    return train_data, eval_data


if __name__ == '__main__':
    # Example usage with the provided generate_data function
    test_sequences = np.random.rand(5, 10, 2)  # Example sequence data
    test_a, test_b = generate_data(test_sequences, window_length=5, num_features=2, train_data_amount=20, eval_data_amount=3)

    print(test_a.shape)
    print(test_a[0])
