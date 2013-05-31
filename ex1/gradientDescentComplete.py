from __future__ import division

#Performs the 1-dimensional gradient descent algorithm
#to minimize the cost function of the test parameter, theta.

import numpy
import computeCostComplete

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
        
        grad_interval = numpy.zeros(numpy.shape(theta)[0])
        for j in range(numpy.shape(theta)[0]):
            grad_interval[j] = numpy.sum(numpy.dot((numpy.dot(X, theta) - y), X[:,j]))

        theta -= grad_interval * (alpha/m)
            
        
        J_history[i] = computeCostComplete.J(X, y, theta)

    return theta