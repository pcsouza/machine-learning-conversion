import numpy
import json

import warmUpExerciseComplete
import plotDataComplete


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