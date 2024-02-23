import tensorflow as tf
from src.vae_model.multi_categorical_vae import tfk

# Change learning rate
learning_rate = 1e-3

def log_likelihood(x, rv_x):
    if isinstance(rv_x, list):
        return [item.log_prob(x) for item in rv_x]
    else:
        return rv_x.log_prob(x)


def neg_log_likelihood(x, rv_x):
    if isinstance(rv_x, list):
        return [-item.log_prob(x) for item in rv_x]
    else:
        return -rv_x.log_prob(x)


def build_vae_from_models(encoder, decoder, learning_rate=learning_rate):
    vae = tfk.Model(inputs=encoder.inputs,
                    outputs=decoder(encoder.outputs[0]))

    vae.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                loss=neg_log_likelihood)

    return vae


def build_conditional_vae_from_models(encoder, decoder, learning_rate=learning_rate):
    vae = tfk.Model(inputs=encoder.inputs,
                    outputs=decoder(encoder.outputs + [encoder.inputs[-1]]))

    vae.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                loss=neg_log_likelihood)

    return vae
