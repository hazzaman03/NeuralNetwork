from tensorflow import keras
import numpy as np

def getData():
    (train_X, train_Y), (test_X, test_Y) = keras.datasets.mnist.load_data()
    train_X = np.reshape(train_X, (-1,28*28,1))
    train_X = np.array(train_X/256, dtype=np.float64)
    test_X = np.reshape(test_X, (-1,28*28, 1))
    test_X = np.array(test_X/256, dtype=np.float64)
    
    
    train_Y = np.array(train_Y, dtype=np.float64)
    test_Y = np.array(test_Y, dtype=np.float64)
    
    train_Y_arr = []
    for num in train_Y:
        new_arr = [0] * 10
        new_arr[int(num)] = 1
        train_Y_arr.append(new_arr)
    train_Y_arr = np.array(train_Y_arr, dtype=np.int8)
        
    test_Y_arr = []
    for num in test_Y:
        new_arr = [0] * 10
        new_arr[int(num)] = 1
        test_Y_arr.append(new_arr)
    test_Y_arr = np.array(test_Y_arr, dtype=np.int8)
    
    return train_X, train_Y_arr, test_X, test_Y_arr

if __name__ == "__main__":
    getData()