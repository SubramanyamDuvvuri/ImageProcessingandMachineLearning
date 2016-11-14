#Importing libraries and frame works
import graphlab
import matplotlib.pyplot as plt


houses = graphlab.SFrame('home_data.gl/')
#graphlab.canvas.set_target()

#houses.show()

plt.figure(1)
plt.plot(houses['sqft_living'],houses['price'],'o')
plt.xlabel('sqft_living')
plt.ylabel('price')
plt.show()
train_data,test_data = houses.random_split(.8,seed=0)
sqft_model = graphlab.linear_regression.create(train_data, target='price', features=['sqft_living'],validation_set=None)


plt.figure(2)
plt.plot(test_data['sqft_living'],test_data['price'],'.',test_data['sqft_living'],sqft_model.predict(test_data),'-')
plt.ylabel('price')
plt.xlabel('sqft_living')
plt.show()

my_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']


my_features_model = graphlab.linear_regression.create(train_data,target='price',features=my_features,validation_set=None)

house1 = houses[houses['id']=='5309101200']
house1.materialize()
print house1

print "price using only one feature"
print sqft_model.predict(house1)
print "price using several features"
print my_features_model.predict(house1)



