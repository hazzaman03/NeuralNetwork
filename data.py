from keras.datasets import mnist
from keras.utils import to_categorical
from os import remove, getcwd
import numpy as np
from scipy.ndimage import rotate
import cv2


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
    for i in range(len(x_train)):
        rotation = np.random.normal(scale=1)
        zoom = np.random.choice(np.linspace(0.70, 0.80, num=20))
        shift_x = np.random.choice([-2, -1, 0, 1, 2])
        shift_y = np.random.choice([-2, -1, 0, 1, 2])
        
        x_train[i] = paddedzoom(x_train[i], zoom)
        x_train[i] = rotate(x_train[i], rotation, reshape=False)
        x_train[i] = shift_image(x_train[i], shift_x, shift_y)
    
    x_train = x_train.reshape(x_train.shape[0], 1, 28*28)
    x_train = x_train.astype('float32')
    x_train /= 255
    
    for i in range(len(x_train)):
        for j in range(len(x_train[i][0])):
            rand = np.random.randint(0,20)
            if rand == 1:
                choice = np.random.choice(np.linspace(0.3, 0.8))
                x_train[i][0][j] = choice
        
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
    try: 
        remove(cwd_str + '/x_train.npy')
        remove(cwd_str + '/y_train.npy')
        remove(cwd_str + '/x_test.npy')
        remove(cwd_str + '/y_test.npy')
    except: 
        print('no current data')
        
    getData()
    
def paddedzoom(img, zoomfactor):

    out  = np.zeros_like(img)
    zoomed = cv2.resize(img, None, fx=zoomfactor, fy=zoomfactor)
    
    h, w = img.shape
    zh, zw = zoomed.shape
        
    if zoomfactor<1:    # zero padded
        out[(h-zh)//2:-(h-zh)//2, (w-zw)//2:-(w-zw)//2] = zoomed
    else:               # clip out
        out = zoomed[(zh-h)//2:-(zh-h)//2, (zw-w)//2:-(zw-w)//2]

    return out

def shift_image(X, dx, dy):
    X = np.roll(X, dy, axis=0)
    X = np.roll(X, dx, axis=1)
    if dy>0:
        X[:dy, :] = 0
    elif dy<0:
        X[dy:, :] = 0
    if dx>0:
        X[:, :dx] = 0
    elif dx<0:
        X[:, dx:] = 0
    return X

if __name__ == "__main__":
    resetData()
