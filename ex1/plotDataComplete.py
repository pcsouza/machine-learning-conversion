import numpy
import matplotlib.pyplot as plt

def plot_data(data):
    plt.plot(data[:,0], data[:,1], 'rx', markersize = 11)
    plt.xlabel("Profit in $10,000s")
    plt.ylabel("Population of city in 10,000s")
    plt.show()
    
