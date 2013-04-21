import numpy
import json

import warmUpExercise
import plotData
import computeCost

## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py
print "Running warmUpExercise.py..."
print "5x5 Identity Matrix:"
print warmUpExercise.identity_matrix()

raw_input("Press Enter to continue")

## ======================= Part 2: Plotting =======================
print "Plotting Data..."
f = open('ex1data1.json', 'r')
data = numpy.array(json.load(f))
f.close()
# Plot Data
# Note: You have to complete the code in plotData.py
plotData.plot_data(data)

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

print "Testing cost calculations with null parameters..."
print "Test cost value: {}".format(computeCost.J(X,y,theta))


