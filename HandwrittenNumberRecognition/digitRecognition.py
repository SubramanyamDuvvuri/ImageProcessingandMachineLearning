from scipy.io import loadmat
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from resizeimage import resizeimage
import random
import warnings
import PIL





warnings.filterwarnings("ignore")

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

#knn.fit(x_train,y_train)
#y_pred = knn.predict(x_test)


##DTC.fit(x_train,y_train)
##y_pred = DTC.predict(x_test)
#SVM.fit (x_train,y_train)
#y_pred = SVM.predict(x_test)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(8, 8), random_state=1)
clf.fit(X, y)
y_pred = clf.predict (x_test)
print metrics.accuracy_score(y_test,y_pred)




k=0
temp = np.zeros((np.sqrt(X.shape[1]),np.sqrt(X.shape[1])))
while (True):
    val = random.randint(0,len(X))
    for i in range(0,20):
        for j in range (0,20):
            temp[i,j]= (X[val,k])
            k=k+1
    y_pred=clf.predict(X[val,:])
    print y_pred
    plt.gca().invert_yaxis()
    plt.contourf(temp.transpose())
    plt.show()

         










