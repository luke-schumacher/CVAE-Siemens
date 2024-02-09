# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Layers for combining `tfp.distributions` and `tf.keras`."""

# import codecs
# import collections
# import functools
# import io
# import pickle

# Dependency imports
# from cloudpickle import CloudPickler
# import numpy as np
# import six
import tensorflow.compat.v2 as tf

# from tensorflow_probability.python import util as tfp_util
# from tensorflow_probability.python.bijectors import fill_scale_tril as fill_scale_tril_lib
# from tensorflow_probability.python.bijectors import transpose as transpose_lib
# from tensorflow_probability.python.distributions import bernoulli as bernoulli_lib
# from tensorflow_probability.python.distributions import categorical as categorical_lib
from tensorflow_probability.python.distributions import distribution as tfd
from tensorflow_probability.python.distributions import independent as independent_lib
# from tensorflow_probability.python.distributions import kullback_leibler as kl_lib
# from tensorflow_probability.python.distributions import logistic as logistic_lib
# from tensorflow_probability.python.distributions import mixture_same_family as mixture_same_family_lib
# from tensorflow_probability.python.distributions import mvn_tril as mvn_tril_lib
# from tensorflow_probability.python.distributions import normal as normal_lib
from tensorflow_probability.python.distributions import onehot_categorical as onehot_categorical_lib
# from tensorflow_probability.python.distributions import poisson as poisson_lib
# from tensorflow_probability.python.distributions import transformed_distribution as transformed_distribution_lib
# from tensorflow_probability.python.distributions import variational_gaussian_process
# as variational_gaussian_process_lib
from tensorflow_probability.python.internal import distribution_util as dist_util

# imports from tfp.layers.distribution_layer (which we want to extend here)
from tensorflow_probability.python.layers.distribution_layer import (DistributionLambda,
                                                                     _event_size, _get_convert_to_tensor_fn,
                                                                     _serialize)


__all__ = [
    'IndependentOneHotCategorical',
]


class IndependentOneHotCategorical(DistributionLambda):
    """An independent one hot categorical Keras layer.

    ### Example

    ```python
    tfd = tfp.distributions
    tfpl = tfp.layers
    tfk = tf.keras
    tfkl = tf.keras.layers

    # Create a stochastic decoder -- e.g., for use in a variational auto-encoder.
    output_shape = [5, 12]
    input_shape = 2

    encoder = tfk.Sequential([
      tfkl.InputLayer(input_shape=input_shape),

      tfkl.Dense(10, activation='relu'),

      tfkl.Flatten(),
      tfkl.Dense(tfpl.IndependentOneHotCategorical.params_size(output_shape)),
      tfpl.IndependentOneHotCategorical(output_shape)
    ])
    ```

    """

    def __init__(self,
                 event_shape=(),
                 convert_to_tensor_fn=tfd.Distribution.sample,
                 validate_args=False,
                 **kwargs):
        """Initialize the `IndependentOneHotCategorical` layer.

        Args:
          event_shape: integer vector `Tensor` representing the shape of single
            draw from this distribution.
          convert_to_tensor_fn: Python `callable` that takes a `tfd.Distribution`
            instance and returns a `tf.Tensor`-like object.
            Default value: `tfd.Distribution.sample`.
          validate_args: Python `bool`, default `False`. When `True` distribution
            parameters are checked for validity despite possibly degrading runtime
            performance. When `False` invalid inputs may silently render incorrect
            outputs.
            Default value: `False`.
          **kwargs: Additional keyword arguments passed to `tf.keras.Layer`.
        """
        convert_to_tensor_fn = _get_convert_to_tensor_fn(convert_to_tensor_fn)

        # If there is a 'make_distribution_fn' keyword argument (e.g., because we
        # are being called from a `from_config` method), remove it.  We pass the
        # distribution function to `DistributionLambda.__init__` below as the first
        # positional argument.
        kwargs.pop('make_distribution_fn', None)

        super(IndependentOneHotCategorical, self).__init__(
            lambda t: IndependentOneHotCategorical.new(t, event_shape, validate_args),
            convert_to_tensor_fn,
            **kwargs)

        self._event_shape = event_shape
        self._convert_to_tensor_fn = convert_to_tensor_fn
        self._validate_args = validate_args

    @staticmethod
    def new(params, event_shape=(), dtype=None, validate_args=False, name=None):
        """Create the distribution instance from a `params` vector."""
        with tf.name_scope(name or 'IndependentOneHotCategorical'):
            params = tf.convert_to_tensor(params, name='params')
            event_shape = dist_util.expand_to_vector(
                tf.convert_to_tensor(
                    event_shape, name='event_shape', dtype_hint=tf.int32),
                tensor_name='event_shape')
            output_shape = tf.concat([
                tf.shape(params)[:-1],
                event_shape,
            ], axis=0)

            dist = independent_lib.Independent(
                onehot_categorical_lib.OneHotCategorical(
                    logits=tf.reshape(params, output_shape),
                    dtype=dtype or params.dtype.base_dtype,
                    validate_args=validate_args),
                reinterpreted_batch_ndims=tf.size(event_shape),
                validate_args=validate_args)

            # we can add members to the distribution, e.g., maybe
            # dist._mean = functools.partial(
            #     _eval_all_one_hot, tfd.Distribution.prob, dist)
            # dist.log_mean = functools.partial(
            #     _eval_all_one_hot, tfd.Distribution.log_prob, dist)

            return dist

    @staticmethod
    def params_size(event_shape=(), name=None):
        """The number of `params` needed to create a single distribution."""
        with tf.name_scope(name or 'IndependentOneHotCategorical_params_size'):
            event_shape = tf.convert_to_tensor(
                event_shape, name='event_shape', dtype_hint=tf.int32)
            return _event_size(
                event_shape, name=name or 'IndependentOneHotCategorical_params_size')

    def get_config(self):
        """Returns the config of this layer.

        NOTE: At the moment, this configuration can only be serialized if the
        Layer's `convert_to_tensor_fn` is a serializable Keras object (i.e.,
        implements `get_config`) or one of the standard values:
         - `Distribution.sample` (or `"sample"`)
         - `Distribution.mean` (or `"mean"`)
         - `Distribution.mode` (or `"mode"`)
         - `Distribution.stddev` (or `"stddev"`)
         - `Distribution.variance` (or `"variance"`)
        """
        config = {
            'event_shape': self._event_shape,
            'convert_to_tensor_fn': _serialize(self._convert_to_tensor_fn),
            'validate_args': self._validate_args
        }
        base_config = super(IndependentOneHotCategorical, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))
