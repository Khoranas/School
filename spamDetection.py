'''Using SVM for spam detection. Requires pre-processing and feature extraction

Notes: Spam detection
    - Minor changes made to reading the file and pre-processing section
'''
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
import pickle

# read the dataset as a txt file with Python's built in open() and read()
datasetPath = 'E:\GCU\TEACHING\AI for Cybersecurity\AI4Cybersecurity\Labs\Week 3\\'
datasetName = 'spam.csv'
with open(datasetPath+datasetName,mode='r') as f:
    rawData = f.readlines()
    # get rid of the first line
    rawData.pop(0)
    
    
# seperate the labels from the messages. Do this for all the datapoints
labels = [] # predefining variable to hold the class labels
messages = [] # predefining variables to hold the email content 

for dataPoint in rawData:
    commaLocation = dataPoint.find(',')
    labels.append(dataPoint[0:commaLocation])
    messages.append(dataPoint[commaLocation+1: ])
    
# Feature selection and extraction 
keyWords = ['free','buy', 'win','claim','offer','urgent']
features = np.zeros((len(messages),len(keyWords))) # or np.zeros((5574,6))

for i, message in enumerate(messages):
    for j, word in enumerate(keyWords):
        features[i,j] = message.lower().count(word)


labels = np.array(labels).reshape((-1,1)) #convering labels to NP aray & reshaping at the same time
dataset = np.hstack((features,labels)) # combining features and labels to create one dataset

df = pd.DataFrame(dataset) # converting dataset to panda dataframe
keyWords.append('labels')
df.to_csv(datasetPath+'dataset.csv', header= keyWords, index=False)#, header=False, index=False) # write to disk as CSV
