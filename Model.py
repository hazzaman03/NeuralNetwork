import numpy as np

from Network import Network
from FClayer import FCLayer
from Activationlayer import ActivationLayer
from Activation import *
from Loss import mse, mse_prime
from data import getData


class Model:
    def __init__(self) -> None:
        # load MNIST from server
        x_train, y_train, x_test, y_test = getData()

        # Network
        self.net = Network()
        
        self.net.add(FCLayer(28*28, 20))
        self.net.add(ActivationLayer(tanh, tanh_prime))
        
        self.net.add(FCLayer(20, 20)) 
        self.net.add(ActivationLayer(tanh, tanh_prime))
        
        self.net.add(FCLayer(20, 20)) 
        self.net.add(ActivationLayer(tanh, tanh_prime))
        
        self.net.add(FCLayer(20, 20)) 
        self.net.add(ActivationLayer(tanh, tanh_prime))
        
        self.net.add(FCLayer(20, 20)) 
        self.net.add(ActivationLayer(tanh, tanh_prime))
        
        self.net.add(FCLayer(20, 20)) 
        self.net.add(ActivationLayer(tanh, tanh_prime))
        
        self.net.add(FCLayer(20, 20)) 
        self.net.add(ActivationLayer(tanh, tanh_prime))
    
        self.net.add(FCLayer(20, 10))                    
        self.net.add(ActivationLayer(tanh, tanh_prime))

        # train on 1000 samples
        # as we didn't implemented mini-batch GD, training will be pretty slow if we update at each iteration on 60000 samples...
        self.net.use(mse, mse_prime)
        self.net.fit(x_train, y_train, epochs=20, learning_rate=0.01)
    
    def predict(self, img):
        prediction = self.net.predict(img)
        prediction = np.exp(prediction)/np.exp(prediction).sum()

        return np.resize(prediction, 10)
        
if __name__ == "__main__":
    model = Model()
    x_train, y_train, x_test, y_test = getData()

    correct = 0
    incorrect = 0
    for x, y in zip(x_test, y_test):
        prediction = model.predict(x)
        
        if np.argmax(prediction) == np.argmax(y):
            correct += 1
        else:
            incorrect += 1
    
    print(correct / (correct + incorrect) * 100)
    
    correct = 0
    incorrect = 0
    for x, y in zip(x_train, y_train):
        prediction = model.predict(x)
        
        if np.argmax(prediction) == np.argmax(y):
            correct += 1
        else:
            incorrect += 1
    
    print(correct / (correct + incorrect) * 100)