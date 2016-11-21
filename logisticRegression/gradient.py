import numpy as np
from sigmoid import sigmoid
def gradient(theta, X, y):  
    theta.shape = (1, 3)
    m = len(y)
    grad = np.zeros(3)

    h = sigmoid(X.dot(theta.T))

    delta = h - y

    l = grad.size

    for i in range(l):
        sumdelta = delta.T.dot(X[:, i])
        grad[i] = (1.0 / m) * sumdelta * - 1

    theta.shape = (3,)

    return grad
