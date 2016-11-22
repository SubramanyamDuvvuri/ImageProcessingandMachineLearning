from scipy.io import loadmat
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

numbers = loadmat ("ex3data1.mat")

X = numbers['X']
y = numbers['y']

logreg = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors=7)
DTC = DecisionTreeClassifier()
SVM = SVC()
#logreg.fit (X,y)

x_train,x_test,y_train,y_test = train_test_split(X,y,random_state=4)

#logreg.fit(x_train,y_train)
#y_pred = logreg.predict(x_test)

knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)


##DTC.fit(x_train,y_train)
##y_pred = DTC.predict(x_test)
#SVM.fit (x_train,y_train)
#y_pred = SVM.predict(x_test)


print metrics.accuracy_score(y_test,y_pred)

xample = X[2288,:]
y_prediction = knn.predict (xample)

print y_prediction
print "Actual value"
print y[2288]



