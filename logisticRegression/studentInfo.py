#Python code to find if the patient has been admitted or not

import numpy as np
import matplotlib.pyplot as plt
from sigmoid import sigmoid
from costCompute import costCompute


#Loading data from file
data = np.loadtxt ('ex2data1.txt',delimiter =',')
x = data[:,0:(data.size/len(data))-1]
y = data[:,(data.size/len(data))-1]


# displaying a scattered plot

#seperating positives and negetives
positive = np.where(y==1)
negetive = np.where(y==0)

# plotting positives and negetives

plt.plot(x[positive,0],x[positive,1],'*',c='b',markersize=10)
plt.plot(x[negetive,0],x[negetive,1],'o',c='r',markersize=10)
plt.xlabel ('Exam Score 1')
plt.ylabel('Exam Score 2')
plt.title ('Grading System')
plt.legend (['Admitted','not admitted'])

##Adding intercept coloumn

ones = np.ones((len(x), (x.size/len(x))+1))
ones[:,1:3] = x [:,0:2]
x=ones

#initializing theta

theta = np.zeros((x.shape[1],1))
j = costCompute ( theta,x,y)





#plt.show()



