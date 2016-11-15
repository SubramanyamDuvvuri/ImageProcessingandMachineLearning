import matplotlib.pyplot as plt
import numpy as np
from Example import Example
from plotData import plotData
from computeCost import computeCost
from gradientDescent import gradientDescent

print "Printing 5X5 identity matrix"

Example()

print "Loading Data...."
data= np.loadtxt("ex1data1.txt",delimiter = ',' )
x=data[:,0]
y =data[:,1]



plt.figure(1)
plotData(x,y)

ones = np.ones((len(y),2))
ones[:,1]=x
x=ones
theta= np.zeros((2,1))

J=computeCost(x,y,theta)

print J
alpha = 0.01
iterations =1500


theta,jHistory = gradientDescent(x, y, theta, alpha, iterations);


y = np.dot(x,theta)

print "Theta found by gradient descent"
print theta

print "plotting regression"

plt.plot(x[:,1],np.dot(x,theta),'-') 

plt.show()


population = np.array((1,9))




prediction = np.dot(population,theta)
print 'For a population of 90000 the predicted profits are'
print prediction*10000







