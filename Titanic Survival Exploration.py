import numpy as np
import pandas as pd
#RMS Titanic data visualization code
from titanic_visualizations import survival_stats
from IPython.display import display
%matplotlib inline
#Load the dataset
in_file='titanic_data.csv'
full_data=pd.read_csv（in_file）
#Print the first few entries of the RMS Titanic data
display(full_data.head())
'''
Since we are interested in the outcome of survival for each passenger or crew member,we can remove the Survived feature from this 
dataset and store it as its own separate variable outcomes.we will use these outcomes as our prediction targets.
'Run the code cell to remove Survived as a feature of the dataset and sotre it in outcomes
'''
#Store the ‘Survived feature in a new variable and remove it from the dataset’
outcomes=full_data['Survived']
data=full_data.drop['Survived',axis=1]
#Show the new dataset with 'Survived' removed
display(data.head())

'''
The very same sample of the RMS Titanic data now shows the Survived feature removed from the DataFrame.Note that data(the passenger data)
'
and outcomes(outcomes of survival) are now paired.That means for any passenger data.loc[i],they have the survival outcome outcome[i]


To measure the performance of our predictions,we need a metric to score our predictions against the true outcomes of survival.Since we are
interested in how accurate our predictions are,we will calculate the proportion of passengers where our prediction of their survival is 
correct.Run the code cell below to create our accuracy_score function and test a prediction on the first five passengers

Think:Out of the first five passengers,if we predict that all of them survived,what would you expect accuracy of our predictions to be?
'''
def accuracy_score(truth,pred):
'    """Returns accuracy score for input truth and predictions."""
    #Ensure that the number of predictions matches number of outcomes
    if len(truth)==len(pred):
        #Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}.".format((truth==pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"
#Test the 'accuarcy_score' function
predictions=pd.Series(np.ones(5,dtype=int))
print accuracy_score(outcomes[:5],predictions)

'''
Tip:if you save an IPython Notebook,the output from runing code blocks will also be saved.However,the state of your workspace will be
reset once a new session is started.Make sure that you run all of the code blocks from your previous session to reestablish variables and 
functions before picking up where you last left off


Make Predictions
if we were told to make a prediction about any passenger aboard the RMS Titanic who we did not know anything about,then the best prediction
we cold make would be that they did not survive.This is because we can assume that a majority of the passengers as a whole did not survie
the ship sinking.
The function below will always predcit that a passenger did not survive

'''
def predictions_0(data):
    """Model with no features.Always predicts a passenger did not survive."""
    predictions=[]
    for _, passenger in data.iterrows():
        #Predict the survival of 'passenger'
        predictions.append(0)
    #Return our predictions
    return pd.Series(predictions)
    #make the predictions
    predictions=predictions_0(data)
    
    '''
    Question 1
    Using the RMS Titanic data,how accurate would a prediction be that none of the passengers survived?
    Hint:Run the code cell below to see the accuracy of this prediction.
    '''
    print accuracy_score(outcomes,predictions)
    
   
'''
Answer:It would be 61.62% accurate to predict that none of the passengers survived.
Let's take a look at whether the feature Sex has any indication of survival rates among passengers using the survival_stats
function.This function is defined in the titanic_visualziations.py Python script included with this project.The first tow
indicates which feature we want to plot survival statistics across.
Run the code cell below to plot the survival outcomes of passengers based on their sex.
'''
survival_stats(data,outcomes,'Sex')

'''
Examining the survival statistics,a large majority of males did not survive the ship sinking.Howere, a majority of females
did survive the ship sinking.Let's build on our previous prediction:If a passenger was female,then we will predict that they survived.Otherwise,we will predict the passenger did not survive.
Fill in the missing code below so that the function will make this prediction
Hint:You can access the values of each feature for a passenger like a dictionary.For example,passenger['Sex'] is the sex of
the passneger.
'''    

def predictions_1(data):
        """Model with one feature:
            -Predict a passenger survived if they are female."""
        predictions=[]
        for _,passenger in data.iterrows():
            #Remove the 'pass' statement below
            #and write your prediction conditions here
            if passenger['Sex']=='female':
                predictions.append(1)
            else:
                predictions.append(0)
        #Return our predictions
        return pd.Series(predictions)
#Make the predictions
predictions=predictions_1(data)//78.68%

'''
Question 2
How accurate would a prediction be that all female passengers survived and the remaining passengers did not survive?
Hint；Run the code cell below to see the accuracy of this prediction
'''
        
print accuracy_score(outcomes,predictions)


'''
Answer:It would be 78.68% accurate to predict that all female passengers survived and remaining passengers did not survive.
Using just the Sex feature for each passenger,we are able to increate the accuracy of our predictions by a significant margin.Now,let's consider using an additional feature to see if we can furthre impive our predictions.Consider,for example,all of the male at the Age of each male,by again using the survival_stats function.This time,we will use a fourth 
parameter to filter out the data so that only passengers with the Sex 'male ' will be included
Run the code cell below to plot the survival outcomes of male passengers based on their age

'''

survival_stats(data,outcomes,'Age',["Sex=='male'"])

'''
Examining the surival statistics,the majority of males younger then 10 survived the ship sinking,whereas most males age 10
or older did nnot survive the ship sinking.Let's continue to bulid on our previous prediction:If a passenger was female,then we will predict they survive.If a passenger was male and younger than 10,then we will also predict they survive.
Otherwise,we will predict thye do not survive.
Fill in the missing code below so that the function will make this prediction
Hint:You can start your implementation of this function using the prediction code you wrote earlier form predictions_1
'''

def predictions_2(data):
    """Model with two features:
        -Predict a passenger survived if they are female.
        -Predict a passenger survived if they are male and younger than 10."""
    predictions=[]
    for _,passenger in data.iterrows():
        if passenger['Sex']=='female' or passenger['Sex']=='male' and passenger['Age']<10"
            predictions.append(1)
        else:
            predictions.append(0)
    #Return our predictions
    return pd.Series(predictions)
#Make the predictions
predictions=predictions_2(data)


'''
Question3
How accurate would a prediction be that all female passengers and all male passengers younger thant 10 survived?
Hint:Run the code cell below to see the accuracy of this prediction.
'''

print accuracy_score(outcomes,predictions)

'''
Answer:It would be 79.35% accurate to predict that all female passengers and all male passengers younger than 10 survived
add the feature Age as a condition in conjunction with Sex imporves the accuracy by a small margin more than with simply 
using the feature Sex alone.Now it is your turn:Find a series of features and conditions to split the data on to obtain an outcome prediction accuracy of at leat 80%.This may require multiple features and multiple levels of conditional statements
to succeed.You can use the same feature multiple time with different conditions
Pclass,Sex,Age,SibSp,and Parch are some suggested features to try
Use the survival_stats function below to examine various survival statistic
Hint:To use mulitple filter conditons,put each conditon in the list passed as the last argument.Example:["Sex=='male'","Age<18"]

'''
survival_stats(data,outcomes,'SibSp',["Sex=='male'","Age<16"])

'''
After exploring the survival statistics visualization,fill in the missing code below so that the function will make your 
prediction.Make sure to keep track of the various features and conditions you tried before arriving at your final prediction model 
Hint:You can start your implementation of this function using the prediction code you wrote earlier from predictions_2

'''

def predictions_3(data):
    """Model with multiple features.Makes a prediction with an accuracy of at least 90%"""
    predictions=[]
    for _,passenger in data.iterrows():
        if passenger['Sex']=='female' or passenger['Sex']=='male' and passenger['Age']<16 and passenger['SibSp']<2:
            predictions.append(1)
        else:
            predictions.append(0)
    #Return our predictions
    return pd.Series(predictions)
#Make the predictions
predictions=predictions_3(data)



'''
Question 4
Describe the steps you took to implement the final predcition model so that it got an accuracy of at leat 80%.What features
did you lool at?Were certain features more informative than others?Which conditions did you use to split the survival outcomes in the data?How accurate are your predictions?
Hint:Run the code cell below to see the accuracy of your predictions.

'''
print accuarcy_score(outcomes,predictions)

'''
Answer:I had to look at all the suggested feature and try them out one by one.Most of the suggested features don't really help except the
number of sibiling or spouses of the passenger,which is what I settled on.If the passenger was male and under 16 and had less than 2 
sibilings then tye were more likely to survive,and if the passenger was young male but had more sibilings then they probably did not 
survive.This prediction had an accuracy of 80.58%

Conclusion
Congratulations on what you are accomplished here! You should now have an alogrithm for predicting whether or not a person survived the 
Titanic disaster,based on thier features,In fact,what you have done here is a manual implementation of a simple machine learing model,
the decision tree.In a decision tree,we split the data into smalller groups,one feature at a time.Each of these splits will result in 
group that are more homogeneous than the original group,so that our predictons become more accurate.The advantage of having a computer do 
things for us is that it will be more echaustive and more precise than our manual exploration abouve.This link provides
another introuction into machine learning using a decision tree

A decision tree is just one of many alogrithms that fall into the category of supervised learning.In this Nanodegree,you will learn about
supervised learning techniques first.In supervised learning,we concern ourselves with using features of data to predict or model things
with objective outcome labels.That is ,each of our datapoints has a true outcome value,wether that be category label like survival 
in the Titanic dataset,or a continuous values like predicting the price of a house.

Question 5
Can you think of an example of where supervised learning can be applied?
Hint:Be sure to note the outcome variable to be predicted and at least two features that might be useful for making the predictions.
Answer:One example would be classifying an vehichle to be different categories of cars.One feature would be the number of doors on the 
vehicle,and other features can include the weight and height of the vehicle.These features can help the algorithm predict if it is 
a mininvan or sprits car

Tip: If we want to share the results of our analysis with others,we are not limited to giving them a copy of the iPython Notebook(.ipynb)
file.We can also export the Notebook output in a form that can be opened even for those without Python installed.From the File menu in the
upper left,go to the Download as submenu.You can then choose a different format that can be viewed more generally,such as HTML
(.html) or PDF (.pdf).You may need additional packages or software to perform these exports.

'''

