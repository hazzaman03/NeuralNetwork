from data import getData
import numpy as np
from PIL import Image 


def showRandomImg():
    x_train, y_train, x_test, y_test = getData()
    
    imgIndex = np.random.randint(0,10000)
    img = x_train[imgIndex]
    img *= 255
    
    img = img.reshape(28,28)
    
    img = Image.fromarray(img) 
    
    img.show()
    
    

if __name__ == "__main__":
    showRandomImg()