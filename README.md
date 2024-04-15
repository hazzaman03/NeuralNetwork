# NeuralNetwork

Creating a neural network from scratch using numpy

# Setup

Create a virtual environment and install requirements:

python -m venv env \    
source env/bin/activate \
pip install -r requirements.txt

Retrieve data and create a model:
To retrieve data, simply run the data.py file. This file will save the data to your local machine to act as a cache. To create a model, simply run the ModelManager.py file, this will also save the created model so you can reuse it. To use the TKinter interface, run the interface.py file. This will open a Tkinter window which you can use to test your trained model. 

# Files

**Activation.py**:
Holds the activation functions for layers. In this case I have implemented the hyperbolic tan activation function.

**ActivationLayer.py**:
Holds the logic for an activation layer. Forward propagation consists of passing the array to the activation function. Backward propagation consists of passing the array through the derivative of the activation function.

**Data.py**:
Uses keras to fetch the data. Then performs a series of noise adding functions. This consists of rotating, zooming, and adding background noise. This will also save the data to act as a cache when retraining models. 

**FClayer.py**:
Holds the logic for a fully connected layer. Holds the layers weights and bias values. Forward propagation consists of matrix multiplying the input with the weights, then adding the biases. Backward propagation consists of calculating the weights error and bias error by matrix multiplying the outputed error by the weights, then this value by the input. These values are then used to adjust the weights and biases. 

**ImageVisualiser.py**:
Helper function that lets the user see how the data has been transformed with noise. 

**interface.py**:
Holds the logic for creating an interface with TKinter. Creates a window, lets the user draw on the window, makes a prediction based on the drawing, then the user is able to reset if they wish. 

**layer.py**:
Abstract class for implementing activation and fully connected layers.

**loss.py**:
Holds the loss functions used for calculating the accuracy of the model. Uses the mean squared error loss function. 

**Model.py**:
Holds the logic for creating a model with the users parameters. The user can add layers and change their size. The user is also able to adjust the learning rate, number of epochs and batch size. 

**Network.py**:
Holds the layers and performs the training of a neural network. Trains the network using a series of epochs which consist of batches. 
