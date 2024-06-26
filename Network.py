import numpy as np

from data import getData
class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    # add layer to network
    def add(self, layer):
        self.layers.append(layer)

    # set loss to use
    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    # predict output for given input
    def predict(self, input_data):
        # sample dimension first
        samples = len(input_data)
        result = []

        # run network over all samples
        for i in range(samples):
            # forward propagation
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result
    
    
    def fit(self, x_train, y_train, epochs, learning_rate, batch_size = 10000):
        # sample dimension first
        samples = len(x_train)
        curr = 0

        # training loop
        for i in range(epochs):
            err = 0
            print(curr)
            for j in range(curr, curr + batch_size):
                # forward propagation
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                # compute loss (for display purpose only)
                err += self.loss(y_train[j], output)

                # backward propagation
                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)
            
            curr += batch_size
            curr = curr if curr + batch_size <= samples else 0

            # calculate average error on all samples
            err /= samples
            print('epoch %d/%d   error=%f' % (i+1, epochs, err))

    # # train the network
    # def fit(self, x_train, y_train, epochs, learning_rate, batch_size = 200):
    #     # sample dimension first
    #     samples = len(x_train)
    #     start = 0
            
    #     # training loop
    #     for i in range(epochs):
    #         err = 0
    #         for j in range(start, start + batch_size):
    #             # forward propagation
    #             output = x_train[j]
    #             for layer in self.layers:
    #                 output = layer.forward_propagation(output)

    #             # compute loss (for display purpose only)
    #             # print(np.argmax(output), np.argmax(y_train[selection[selection[j]]]))
    #             err += self.loss(y_train[j], output)

    #             # backward propagation
    #             error = self.loss_prime(y_train[j], output)
    #             for layer in reversed(self.layers):
    #                 error = layer.backward_propagation(error, learning_rate)
    #         # self.test_network()
    #         start = start + batch_size if start + batch_size < samples else 0
            

    #         # calculate average error on all samples
    #         err /= samples
    #         print('epoch %d/%d   error=%f' % (i+1, epochs, err))
            
    
    def test_network(self):
        x_train, y_train, x_test, y_test = getData()

        correct = 0
        incorrect = 0
        for x, y in zip(x_test, y_test):
            prediction = self.predict(x)
            
            if np.argmax(prediction) == np.argmax(y):
                correct += 1
            else:
                incorrect += 1
        
        print(correct / (correct + incorrect) * 100)
        