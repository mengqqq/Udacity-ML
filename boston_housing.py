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
implementation is working successfully.The print statements will show the statistics you calculate!'''
#Number of houses in the dataset
total_houses=housing_features.shape[0]
#Number of features in the dataset
total_features=housing_features.shpae[1]
#Minimun housing value in the dataset
minimun_price=np.min(housing_prices)
#Maximun housing value in the dataset
maximum_price=np.max(housing_prices)
"#Mean house value of the dataset
mean_price=np.mean(housing_prices)
#Median house value of the dataset
median_price=np.median(housing_prices)
#Standard deviation of housing values of the dataset
std_dev=np.std(housing_prices)
#Show the calculated statistics
print "Boston Housing dataset statistics (in $1000's):\n"
print "Total number of houses:",totao_houses

print "Total number of features:",total_features
"print "Minimum house price:",minimun_price
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
Randomly shuffle the input data X and target labels (housing values)y
Split the data into training and testing subsets,holding 30% of the data for testing.
If you use any functions not already acessible from the imported libraries above,remember to include your import statement below as well!
Ensure that you habe executed the code block once you are done.You will know the shuffle_split_data function is working if the datament
"Successfully shuffled and split the data!" is printed
'''
#Put any import statements you need for this code block here
from sklearn.cross_validation import train_test_split
def shuffle_split_data(X,y):
     """Shufflea and splits data into 70% training and 30% testing subsets,
        then returns the training and testing subsets"""
    #Shuffle and split the data
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
    #Return the training and testing data subsets
    return X_train,y_train,X_test,y_test
    #Test shuffle_split_data
try：
    X_train,y_train,X_test,y_test=shuffle_split_data(housing_features,housing_prices)
    print "Successfully shuffled and split the data!"
except:
    print "Somenthing went wrong with shuffling and splitting the data."
'''
Question 3
Why do we split the data into training and testing subsets for our modle?
Answer:Our model has to perform well when fed previously unseen data.We will train the mmodel with training set and so performance 
measures on that smae set will not be representative of the quality of the modle.We need to evaluate its performance on a dataset that 
was not used to train the modle:the testing subset.

Step 3
In the code block below ,you wil need to implement code so that the performance_metric function does the following:
 Perform a total error calculaton between the true values of the y labels y_true and the predicted values of the y lables y_predict
You will need to first choose an appropriate performance metric for this problem.See the sklearn metrics documentation to vies a list
of avaiable metric functions.
Hint:Look at the question below to see a list of the metrics that were covered in the supporting course for this project
Once you have determined which metric you will use,remember ot include the necessary import statement as well!
Ensure that you habe executed the code block once you are done.You will know the performance_metric function is working if the 
statment "Successfully performed a metric calculation !" is printed

'''
#Put any import statement you need for this code block here
from sklearn import metrics 
def performance_metric(y_true,y_predict):
  """Calculates and returns the total error between true and predicted values
     based on a performance metric chosen by the student"""
    error=metrics.mean_squared_error(y_true,y_predict)
    return error
#Test performance_metric
try:
    total_error=performance_metric(y_train,y_train)
    print "Successfully performed a metric calculation!"
except:
    print "Something went wrong with performing a metric calculation"
'''
Question 4
Which performance metric below did you find was most appropriate for predicting housing prices and analyzing the total error.Why?
Accuracy
Precision
Recall
F1 Score
Mean Squared Error (MSE)
Mean Absolute Error(MAE)
Answer:I chose to use the mean squared error.Of the avaiable list,only the last two apply to regression,the other four being useful for 
classificaton problems.Some of the advantages of using MSE over MAE is that,being quadratic,it "penalizes" greater error over smaller ones,
but more important:its quadrature means we can use its derivative to tind valuse for parameters tha minimize it.

Step 4
In hte code block below,you will need to implement code so that the fit_model function does the following:
Create a scoring function using the same  performance metric as in Step 2.See the sklearn make scorer documentation.
Build a GridSearchCV object using regressor,parameters,and scoreing_function,See the sklearn documentation on GridSearchCV
When building the scoring function and GridSearchCV object,be sure that you read the parameters documentation thoroughly.It is nnot 
always the case that a default parameter for a function is the appropriate setting for the problem you are working on 
Since you are using sklearn functions,rememeber to include the necessary import statements below as well!
Ensure that you habe executed the code block once you are done.You will know the fit_model function is working if the datement 
"Successfully fit a model  to the data" is printed












'''







    














