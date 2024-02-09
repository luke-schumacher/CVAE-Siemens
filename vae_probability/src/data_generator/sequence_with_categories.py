import numpy as np


def generate_data(window_length=10,
                  num_features=2,
                  train_data_amount=25000,
                  eval_data_amount=5000,
                  ):

    def random_fill(data):
        for i in range(data.shape[0]):
            random_pos = np.random.choice(range(data.shape[2]))
            data[i, :, random_pos] = 1.0

        return data

    train_data = np.zeros((train_data_amount, window_length, num_features))
    eval_data = np.zeros((eval_data_amount, window_length, num_features))

    train_data = random_fill(train_data)
    eval_data = random_fill(eval_data)

    np.random.shuffle(train_data)
    np.random.shuffle(eval_data)

    return train_data, eval_data


if __name__ == '__main__':
    test_a, test_b = generate_data(5, 10, 20, 3)

    print(test_a.shape)
    print(test_a[0])
