from tensorflow import keras

def getData():
    (train_X, train_Y), (test_X, test_Y) = keras.datasets.mnist.load_data()
    
    return train_X, train_Y, test_X, test_Y