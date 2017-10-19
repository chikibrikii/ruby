import time
import warnings
import book
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.cross_validation import  train_test_split
from matplotlib import pyplot as plt
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential


def build_model(layers):
    model = Sequential()

    model.add(LSTM(
        input_dim = layers[0],
        output_dim = layers[1],
        return_sequences = True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],
        return_sequences = False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim = layers[3]))
    model.add(Activation("linear"))

    start = time.time()
    model.compile(loss="mse", optimizer="rmsprop")
    print("> Compilation Time : ", time.time() - start)
    
    return model

def normalise_windows(window_data):
    normalised_data = []
    for window in window_data:
        for p in window:
            normalised window = float(p) / float(window[0]) - 1
        normalised_data.append(normalised_window)
    
    return normalised_data