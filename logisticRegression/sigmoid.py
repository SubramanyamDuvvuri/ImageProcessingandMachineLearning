
import numpy as np

def sigmoid (x):
    x = np.array(x)
    g = np.zeros(x.size)
    g=np.divide(1,(1+np.exp(-x)))
    return g
    
