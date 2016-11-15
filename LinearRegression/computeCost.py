#Evaluate the linear regression
import numpy as np
#from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
def computeCost(X, y, theta):
    '''
    Comput cost for linear regression
    '''
    #Number of training samples
    m = len(y)

    predictions = np.dot(X,theta).flatten()

    sqErrors = (predictions - y) ** 2

    J = (1.0 / (2 * m)) * sqErrors.sum()

    return J
