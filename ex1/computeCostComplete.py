import numpy

# J(X, y, theta) computes the cost of using theta as the
# parameter for linear regression to fit the data points in X and y

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
# by completing the function below

def J(X, y, theta):
    J = 0
    m = y.shape[0]
    
    for i in range(m):
        J += (numpy.dot(theta, X[i]) - y[i])**2
    return J/(2*m)

    

