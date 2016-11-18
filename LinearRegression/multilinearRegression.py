##
#Linear regression for multiple features
#

import numpy as np
import matplotlib.pyplot as plt
from computeCost import computeCost
from gradientDescent import gradientDescent
from normalize import normalize
print "Loading Data...."
data= np.loadtxt("ex1data2.txt",delimiter = ',' )

x = np.zeros((len(data),2))
x[:,0]=data[:,0]
x[:,1]=data[:,1]
y =data[:,2]

# Adding bias

ones  = np.ones((len(x),3))

ones[:,1]=x[:,0]
ones[:,2]=x[:,1]
x = ones


#Computing cost
alpha = 0.01;
num_iters = 400;
theta = np.zeros((3, 1));
J = computeCost(x,y,theta)
print J

theta,Jhistory = gradientDescent(x,y,theta,alpha,num_iters)
print theta


