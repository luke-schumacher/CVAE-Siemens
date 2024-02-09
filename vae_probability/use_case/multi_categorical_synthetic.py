import tensorflow as tf

from src.data_generator.sequence_with_categories import generate_data
from src.vae_model.multi_categorical_vae import build_vae_submodels
from src.vae_model.common_functions import build_vae_from_models


def main(epochs=1):
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print(tf.test.gpu_device_name())

    if tf.test.gpu_device_name() != '/device:GPU:0':
        print('WARNING: GPU device not found.')
    else:
        print('SUCCESS: Found GPU: {}'.format(tf.test.gpu_device_name()))

    window_length = 5
    num_categories = 10

    input_shape = (window_length, num_categories)

    encoded_size = 2
    base_depth = 8

    encoder, decoder = build_vae_submodels(input_shape,
                                           encoded_size,
                                           base_depth)

    print(encoder.summary())
    print(decoder.summary())

    vae = build_vae_from_models(encoder, decoder)

    print(vae.summary())

    train_data, eval_data = generate_data(window_length=window_length,
                                          num_features=num_categories,
                                          train_data_amount=2500,
                                          eval_data_amount=1000,
                                          )

    _ = vae.fit(x=train_data,
                y=train_data,
                epochs=epochs,
                validation_data=(train_data, train_data))

    example_data_points = eval_data[:1]
    example_output_distributions = vae(example_data_points)

    # Samples
    num_samples = 5
    for n_sample in range(num_samples):
        print(f"Sample {n_sample}")
        print(example_output_distributions.sample())


if __name__ == '__main__':
    main(epochs=40)
