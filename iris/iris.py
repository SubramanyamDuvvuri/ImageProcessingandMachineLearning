from sklearn.datasets import load_iris # importing dataset
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn.neighbors import KNeighborsClassifier #Importing models
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.cross_validation import train_test_split

from sklearn import metrics


iris = load_iris()

X = iris.data   # matrix
y= iris.target  # vector


print "Using KNN..."
knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(X,y)

y_predict = knn.predict([1,2,3,4])
print y_predict


print "Using Logistic Regression"
logreg = LogisticRegression()
logreg.fit(X,y)
y_predict = knn.predict(X)
print y_predict

print "Accuracy is"
print metrics.accuracy_score(y,y_predict)

#Importing new data
print "Importing new data"

data = pd.read_csv("http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv",index_col=0)

print "Plotting the data"
sb.pairplot(data,x_vars = ['TV','Radio','Newspaper'],y_vars='Sales',size=7,aspect =0.7)
sb.pairplot(data,x_vars = ['TV','Radio','Newspaper'],y_vars='Sales',size=7,aspect =0.7,kind='reg') # Plotting regression

print "Performing cross validation"
x_train,x_test,y_train,y_test = train_test_split(X,y,random_state=4)

linreg = LinearRegression ()
linreg.fit (x_train,y_train)

y_predict = linreg.predict(x_test)

print np.sqrt(metrics.mean_squared_error(y_test,y_predict))
print "Calculated RMSE"


sb.plt.show()








