#Python code to find if the patient has been admitted or not
global numpy
import numpy as np
import matplotlib.pyplot as plt
from sigmoid import sigmoid
from costCompute import costCompute
from gradient import gradient
from  predict import predict
import scipy.optimize as opt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import warnings
warnings.filterwarnings('ignore')

#Loading data from file

data = np.loadtxt ('ex2data1.txt',delimiter =',')
X = data[:,0:(data.size/len(data))-1]
y = data[:,(data.size/len(data))-1]


# displaying a scattered plot

#seperating positives and negetives
positive = np.where(y==1)
negetive = np.where(y==0)

# plotting positives and negetives

plt.plot(X[positive,0],X[positive,1],'*',c='b',markersize=10)
plt.plot(X[negetive,0],X[negetive,1],'o',c='r',markersize=10)
plt.xlabel ('Exam Score 1')
plt.ylabel('Exam Score 2')
plt.title ('Grading System')
plt.legend (['Admitted','not admitted'])
##
####Adding intercept coloumn
##
##ones = np.ones((len(x), (x.size/len(x))+1))
##ones[:,1:3] = x [:,0:2]
##x=ones
##
###initializing theta
##
##theta = np.zeros((x.shape[1],1))
##j = costCompute ( theta,x,y)
##grad = gradient(theta,x,y)
##result = opt.fmin_tnc(func=j, x0=theta, fprime=gradient, args=(x, y))  
##
##
##
##
###plt.show()

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X,y)

y_predict = knn.predict([34,65])

print y_predict
#X = np.concatenate((X[:,0],X[:,1]), axis = 0)
#Y = np.array([0]*100 + [1]*100)

C = 2 # SVM regularization parameter
clf = svm.SVC(kernel = 'linear',  gamma=0.7, C=C )
clf.fit(X, y)
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(X.min(), X.max())
yy = a * xx - (clf.intercept_[0]) / w[1]

plt.plot(xx, yy, 'k-')


plt.show()







