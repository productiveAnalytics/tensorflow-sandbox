# tensorflow-sandbox
Deep Learning using TensorFlow, Keras and Python 3 

Run from root folder as:
  python .\Scripts\generate_house_price_data.py

It will generate csv data as:
  .\Data\house_price_data.csv

Use: https://colab.research.google.com/

Skeleton code:

import tensorflow as tf
import numpy as np
from tensorflow import keras

# Build model with Sequential layers
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Set Optimizer function and Loss function
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float) # 0.5 + (x * 0.5)

# Try to fit model with given data
model.fit(xs, ys, epochs=1000) # epochs means number of tries to fit the model

# Predict!
print(model.predict([7.0])) # Expected Value: 3.5
