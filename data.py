from tensorflow import keras
import numpy as np

def getData():
    (train_X, train_Y), (test_X, test_Y) = keras.datasets.mnist.load_data()
    train_X = np.array(train_X/256, dtype=np.float64)
    train_Y = np.array(train_Y/256, dtype=np.float64)
    test_X = np.array(test_X/256, dtype=np.float64)
    test_Y = np.array(test_Y/256, dtype=np.float64)
    
    return train_X, train_Y, test_X, test_Y
