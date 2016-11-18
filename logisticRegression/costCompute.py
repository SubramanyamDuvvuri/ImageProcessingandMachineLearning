import numpy as np
from sigmoid import sigmoid
def costCompute(theta,x,y):
    m =x.shape[0]
    y1=y
    y.shape=(len(y),1)
    prediction = np.multiply(-y,np.log(sigmoid(np.dot(x,theta)))) - np.multiply((1-y),np.log(1-sigmoid(np.dot(x,theta))))
    prediction_sum=prediction.sum()
    j = prediction_sum/m
    grad = (np.dot(x.transpose(),sigmoid(np.dot(x,theta))-y1))/m
    #print grad
    return (j)

                                                                                 
