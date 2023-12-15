import numpy as np
# from data import getData
class Network:
    INPUT = 28 * 28
    OUTPUT = 10
    LEARNING_RATE = 0.05
    LAYER_LENGTH = 5
    
    def __init__(self) -> None:
        self.layers = [Layer(self.INPUT, self.LAYER_LENGTH), Layer(self.LAYER_LENGTH, self.LAYER_LENGTH), Layer(self.LAYER_LENGTH, self.OUTPUT)]

    def predict(self, img):
        res = img 
        
        for i in self.layers:
            res = self.soft_max(np.dot(i.weights, res) + i.biases)
        print(res)
        
    def sigmoid(self, x):
        return np.divide(1, 1 + np.exp(-x))
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def soft_max(self, x):
        return np.divide(np.exp(x), np.sum(np.exp(x)))
    
class Layer:
    def __init__(self, length, previous) -> None:
        self.length = length
        self.previous = previous
        
        self.weights = 0.01 * np.random.random((self.previous, self.length))
        self.biases = np.zeros((self.previous, 1))
        
if __name__ == "__main__":
    network = Network()
    network.predict(np.random.random((28*28,1)))
    
    # train_X, train_Y, test_X, test_Y = getData()
    
    # np.save('trainx_sample', train_X[:100])
    # np.save('trainy_sample', train_Y[:100])
    # np.save('testx_sample', test_X[:100])
    # np.save('testy_sample', test_Y[:100])
    
    # train_X, train_Y, test_X, test_Y = np.load('trainx_sample.npy'), np.load('trainy_sample.npy'), np.load('testx_sample.npy'), np.load('testy_sample.npy')
    