import numpy
import json
import matplotlib.pyplot as plt

import warmUpExerciseComplete
import plotDataComplete
import computeCostComplete
import gradientDescentComplete


## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py
print "Running warmUpExercise.py..."
print "5x5 Identity Matrix:"
print warmUpExerciseComplete.identity_matrix()

raw_input("Press Enter to continue")

## ======================= Part 2: Plotting =======================
print "Plotting Data..."
f = open('ex1data1.json', 'r')
data = numpy.array(json.load(f))
f.close()
# Plot Data
# Note: You have to complete the code in plotData.py
plotDataComplete.plot_data(data)

raw_input("Press Enter to continue")

## =================== Part 3: Gradient descent ===================
print "Running Gradient Descent ..."
m = data.shape[0]  # Length of the data array
X = numpy.array([numpy.ones(m).T, data[:,0]]).T #Add a column of ones to X
y = data[:,1]
theta = numpy.zeros(2) #initialize fitting parameters

# Gradient descent settings
iterations = 1500
alpha = .01

# Test cost calculation
print "Testing cost calculations with null parameters..."
print "Test cost value: {}".format(computeCostComplete.J(X,y,theta))

# Run gradient descent
theta_final = gradientDescentComplete.grad_des(X, y, theta, alpha, iterations)
print "Parameters found by gradient descent: {}, {}".format(theta_final[0], theta_final[1])

#Plot found regression
plt.plot(data[:,0], data[:,1], 'rx', markersize = 11)
plt.plot(data[:,0], numpy.dot(theta_final, X.T))
plt.ylabel("Profit in $10,000s")
plt.xlabel("Population of city in 10,000s")
plt.legend(("Training Data", "Linear Regression"), "lower right")
plt.show()

#Make predictions for population sizes of 35,000 and 70,000
print "\n"
print "For population = 35,000 we predict a profit of ${}.".format(int(numpy.dot([1, 3.5], theta_final)*10000))
print "\n"
print "for population = 70,000 we predict a profit of ${}.".format(int(numpy.dot([1, 7], theta_final)*10000))
