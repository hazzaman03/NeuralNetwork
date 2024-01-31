from keras.datasets import mnist
from keras.utils import to_categorical
from os import remove, getcwd
import numpy as np

def getData():
    
    try: 
        x_train = np.load('x_train.npy')
        y_train = np.load('y_train.npy')
        x_test = np.load('x_test.npy')
        y_test = np.load('y_test.npy')
        
        return x_train, y_train, x_test, y_test
    except:
        pass
    
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # training data : 60000 samples
    # reshape and normalize input data
    x_train = x_train.reshape(x_train.shape[0], 1, 28*28)
    x_train = x_train.astype('float32')
    x_train /= 255
    for i in range(len(x_train)):
        for j in range(len(x_train[i][0])):
            rand = np.random.randint(0,15)
            if rand == 1:
                x_train[i][0][j] = np.random.choice([0.4,0.5,0.6,0.7,0.8])
        
    # encode output which is a number in range [0,9] into a vector of size 10
    # e.g. number 3 will become [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    y_train = to_categorical(y_train)
    
    # same for test data : 10000 samples
    x_test = x_test.reshape(x_test.shape[0], 1, 28*28)
    x_test = x_test.astype('float32')
    x_test /= 255
    y_test = to_categorical(y_test)
    
    np.save('x_train', x_train)
    np.save('y_train', y_train)
    np.save('x_test', x_test)
    np.save('y_test', y_test)
    
    np.random.shuffle(x_train)
    
    return x_train, y_train, x_test, y_test

def resetData():
    cwd_str = getcwd()
    remove(cwd_str + '/x_train.npy')
    remove(cwd_str + '/y_train.npy')
    remove(cwd_str + '/x_test.npy')
    remove(cwd_str + '/y_test.npy')
    getData()

if __name__ == "__main__":
    resetData()
