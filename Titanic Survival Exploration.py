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
    
'   
    print accuracy_score(outcomes,predictions)
    
    survival_stats(data,outcomes,'Sex')
    
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


        
    
