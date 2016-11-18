import numpy as np
from sigmoid import sigmoid
def costCompute(theta,x,y):
    m =x.shape[0]
    prediction = np.dot(-y,np.log10(sigmoid(np.dot(x,theta)))) - np.dot((1-y),np.log10(1-sigmoid(np.dot(x,theta))))
    #prediction_sum=prediction.sum
    print prediction
    j = prediction/m                                                                          
    return j

                                                                                 
