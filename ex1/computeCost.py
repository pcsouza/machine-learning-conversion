import numpy

# J(X, y, theta) computes the cost of using theta as the
# parameter for linear regression to fit the data points in X and y

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
# by completing the function below

def J(X, y, theta):
    
    # Initialize some useful values
    J = 0
    m = y.shape[0]

    return J