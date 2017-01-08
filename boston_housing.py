Importing a few necessary libraries
import numpy as np
import matplotlibpyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
#Make matplotlib show our plots inline (nicely formated in the notebook)
%matplotlib inline
#Create our client's feature set for which we will be predicting a selling price
CLIENT_FEATURES=[[11.95,0.00,18.100,5.6090,90.00,1.385,24,680.0,20.20,332.09,12.13]]
#Load the Boston Housing dataset into the city_data variable
city_data=datasets.load_boston()

#Initialize the housing prices and housing features
housing_prices=city_data.target
housing_features=city_data.data
print "Boston Housing dataset loaded successfully!"

'''
Statisticalf Analysis and Data Exploration
In this first section of the project,you will quickly investigate a few basic statistics about the dataset you are working with.In addition,
you will look at the client's feature set in CLIENT_FEATURES and see how this particular sample relates to the features of the dataset.
Familiarizing yourself with the data through an explorative process is a fundamental practice to help you better understand your results.

Step 1
In the code block below ,use the imported numpy library to calculate the requested statistics.You will need to replace each None you
find with the appropriate numpy coding for the proper statistic to be printed.Be sure to execute the code block each time to test is your
implementation is working successfully.The print statements will show the statistics you calculate!
'''
#Number of houses in the dataset
total_houses=housing_features.shape[0]
#Number of features in the dataset
total_features=housing_features.shpae[1]
#Minimun housing value in the dataset
minimun_price=np.min(housing_prices)
#Maximun housing value in the dataset
maximum_price=np.max(housing_prices)
#Mean house value of the dataset
mean_price=np.mean(housing_prices)
#Median house value of the dataset
median_price=np.median(housing_prices)
#Standard deviation of housing values of the dataset
std_dev=np.std(housing_prices)
#Show the calculated statistics
print "Boston Housing dataset statistics (in $1000's):\n"
print "Total number of houses:",totao_houses
print "Total number of features:",total_features
print "Minimum house price:",minimun_price
print "Maximum house price:",maximum_price
print "Mean house price:{0:.3f}".format(mean_price)
print "Median house price:",median_price
print "Standard deviation of house price:{0：.3f}".format(std_dev)
'''
Question 1
As a reminder,you can view a description of the Boston Housing dataset here,where you can find the different features under Attribute 
Information.The MEDV attribute relates to the values stored in our housing_prices variable,so we do not consider that a feature of the 
data.
of the features available for each data point,choose three that you feel are significant and give a brief description for each of what 
they measure
Remember,you can double click the text box below to add your answer!
Answer:Three predictors that may be signigicant are:the per capita crime rate(CRIM),the Charle River variable (CHAS),and the distance
to employment hubs(DIS).These variables measure the per capita crime rate per town,the proximity to the Charles River(it si actually a 
classifier,so it is measured through a dummy variabel which take the values 1if the house is by the river,0 if not),and the weighted 
distances to 5 major employment centers.
Question 2
Using your client's feature set CLIENT_FEATURES,which values correspond with the feature you've chosen above?
Hint:Run the code block below to see the client's data

'''
import pandas as pd
print pd.DataFrame(CLIENT_FEATURES,columns=city_data.feature_names)

'''
Evaluating Model Performance
In this second section of the project,you will begin to develop the tools necessary for a model to make a prediction.Being able to 
accurately evaluate each modle's performance through the use of these tools helps to greatly reinforce the confidence in your predictions.
Step2
In the code block below,you will need to implement code so that the shuffle_split_data function does the following:
r
'''

















