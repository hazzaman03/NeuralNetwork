from Model import Model
from data import getData
import numpy as np
import pickle
from os import remove, getcwd


def getModel():
    try: 
        with open('model_data.pkl', 'rb') as inp:
            model = pickle.load(inp)
            return model
    except:
        pass
    
    with open('model_data.pkl', 'wb') as outp:
        model = Model()
        pickle.dump(model, outp, pickle.HIGHEST_PROTOCOL)
        
    return model

def resetModel():
    cwd_str = getcwd()
    try: 
        remove(cwd_str + '/model_data.pkl')
    except:
        print('no model found')
        
    return getModel()

if __name__ == "__main__":
    model = resetModel()
    x_train, y_train, x_test, y_test = getData()

    # for x, y in zip(x_test[:10], y_test[:10]):
    #     prediction = model.predict(x)
        
    #     print(f"{np.argmax(y) + 1}:{np.amax(prediction)}")
    