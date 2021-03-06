#Performs the 1-dimensional gradient descent algorithm
#to minimize the cost function of the test parameter, theta.

import numpy
import computeCost

def grad_des(X, y, theta, alpha, num_iters):
    m = y.shape[0]  # Length of the data array
    J_history = numpy.zeros(num_iters)
    
    for i in range(num_iters):
        # ====================== YOUR CODE HERE ======================
        # Instructions: Perform a single gradient step on the parameter vector
        #               theta. 
        #
        # Hint: While debugging, it can be useful to print out the values
        #       of the cost function (computeCost) and gradient here.
        
        
        J_history[i] = computeCost.J(X, y, theta)
        
    return theta