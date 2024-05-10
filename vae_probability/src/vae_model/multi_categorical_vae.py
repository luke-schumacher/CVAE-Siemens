import tensorflow as tf
import tensorflow_probability as tfp
import src.tfp_layers.distribution_layer as tfpol

tfd = tfp.distributions
tfk = tf.keras #type: ignore
tfkl = tfk.layers
tfpl = tfp.layers


def build_vae_submodels(input_shape,
                        encoded_size,
                        base_depth):

    prior = tfd.Independent(tfd.Normal(loc=tf.zeros(encoded_size), scale=1),
                            reinterpreted_batch_ndims=1)

    encoder = tfk.Sequential([
        tfkl.InputLayer(input_shape=input_shape),

        # pre processing
        tfkl.Lambda(lambda x: tf.cast(x, tf.float32)),

        # # latent parameter computation
        tfkl.GRU(base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(2 * base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(2 * base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.Flatten(),

        # latent distribution
        tfkl.Dense(tfpl.MultivariateNormalTriL.params_size(encoded_size),
                   activation=None),
        tfpl.MultivariateNormalTriL(
            encoded_size,
            activity_regularizer=tfpl.KLDivergenceRegularizer(prior)),
    ], name="Encoder")

    decoder = tfk.Sequential([
        tfkl.InputLayer(input_shape=[encoded_size]),

        # pre processing
        tfkl.Dense(input_shape[0] * base_depth, activation=tf.nn.leaky_relu),
        tfkl.Reshape([input_shape[0], base_depth]),

        # # reconstruction parameter computation
        tfkl.GRU(2 * base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(2 * base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.GRU(2, activation=tf.nn.leaky_relu, return_sequences=True),
        tfkl.Flatten(),

        # reconstruction distribution
        tfkl.Dense(tfpol.IndependentOneHotCategorical.params_size(input_shape),
                   activation=None),
        tfpol.IndependentOneHotCategorical(input_shape),
    ], name="Decoder")

    decoder2 = tfk.Sequential([
    tfkl.InputLayer(input_shape=[encoded_size]),

    # Dense layer after reshaping
    tfkl.Dense(input_shape[0] * base_depth // 2, activation=tf.nn.leaky_relu),
    tfkl.Reshape([input_shape[0], base_depth // 2]),

    # Additional GRU layers in the decoder
    tfkl.GRU(2 * base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
    tfkl.GRU(3 * base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
    tfkl.GRU(base_depth, activation=tf.nn.leaky_relu, return_sequences=True),
    tfkl.GRU(base_depth // 2, activation=tf.nn.leaky_relu, return_sequences=True),

    # Flatten layer
    tfkl.Flatten(),

    # Simplified dense layer
    tfkl.Dense(tfpol.IndependentOneHotCategorical.params_size(input_shape),
               activation=None),
    tfpol.IndependentOneHotCategorical(input_shape),
    ], name="Decoder2")

    sampler = tfk.Sequential([
        
        decoder2
         
    ], name ="Sampler")
    
    return encoder, decoder2, sampler


