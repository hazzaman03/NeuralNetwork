import numpy as np

from Network import Network
from FClayer import FCLayer
from Activationlayer import ActivationLayer
from Activation import *
from Loss import mse, mse_prime

from keras.datasets import mnist
from keras.utils import to_categorical

class Model:
    def __init__(self) -> None:
        # load MNIST from server
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        # training data : 60000 samples
        # reshape and normalize input data
        x_train = x_train.reshape(x_train.shape[0], 1, 28*28)
        x_train = x_train.astype('float32')
        x_train /= 255
        for i in range(len(x_train)):
            for j in range(len(x_train[i][0])):
                rand = np.random.randint(0,5)
                if rand == 1:
                    x_train[i][0][j] = np.random.rand()
        
        
        
        # encode output which is a number in range [0,9] into a vector of size 10
        # e.g. number 3 will become [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        y_train = to_categorical(y_train)

        # same for test data : 10000 samples
        x_test = x_test.reshape(x_test.shape[0], 1, 28*28)
        x_test = x_test.astype('float32')
        x_test /= 255
        y_test = to_categorical(y_test)

        # Network
        self.net = Network()
        self.net.add(FCLayer(28*28, 100))                # input_shape=(1, 28*28)    ;   output_shape=(1, 100)
        self.net.add(ActivationLayer(tanh, tanh_prime))
        self.net.add(FCLayer(100, 100))                   # input_shape=(1, 100)      ;   output_shape=(1, 50)
        self.net.add(ActivationLayer(tanh, tanh_prime))
        self.net.add(FCLayer(100, 10))                    # input_shape=(1, 50)       ;   output_shape=(1, 10)
        self.net.add(ActivationLayer(tanh, tanh_prime))

        # train on 1000 samples
        # as we didn't implemented mini-batch GD, training will be pretty slow if we update at each iteration on 60000 samples...
        self.net.use(mse, mse_prime)
        self.net.fit(x_train[0:1000], y_train[0:1000], epochs=200, learning_rate=0.01)
    
    def predict(self, img):
        prediction = self.net.predict(img)
        prediction = np.exp(prediction)/np.exp(prediction).sum()

        return np.resize(prediction, 10)
        
if __name__ == "__main__":
    model = Model()