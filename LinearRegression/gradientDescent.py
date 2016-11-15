import numpy as np
from computeCost import computeCost

def gradientDescent(X, y, theta, alpha, num_iters):
    '''
    Performs gradient descent to learn theta
    by taking num_items gradient steps with learning
    rate alpha
    '''
    m = y.size
    J_history = np.zeros(shape=(num_iters, 1))
    error =np.ones((len(theta),1))
    


    for i in range(num_iters):

        predictions = np.dot(X,theta).flatten()
        val = (predictions -y)
        for j in range(0,len(theta)):
            temp =val * X[:,j]
            error[j,0] = temp.sum()
            theta[j,0] = theta[j][0] - alpha * (1.0 / m) * error[j,0].sum()
        

        J_history[i, 0] = computeCost(X, y, theta)

    return theta, J_history
