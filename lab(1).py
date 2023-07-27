
import warnings; warnings.filterwarnings("ignore") # ignore this line
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# read the dataset as a txt file with Python's built in open() and read()
datasetName = 'spam.csv'
data = pd.read_csv(datasetName) # read the data

# convert data to numpy
data = np.array(data)

# Extractnig features and labels
features = data[:,0:-1]
labels = data[:,-1]

# pre-processing the labels and features
encoder = LabelEncoder()
labels = encoder.fit_transform(labels)

# splitting data to training and testing 
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2)

model = Perceptron()
model.fit(train_features,train_labels) # train the model using training dataset

weights = np.asarray(model.coef_)
bias = np.asanyarray(model.intercept_)

# train accuracy
print(model.score(train_features, train_labels))

predictions = model.predict(test_features) # predict using test dataset
accScore = accuracy_score(test_labels, predictions)
print(f'Spam detection accuracy: {accScore*100:0.2f}%')

precScore = precision_score(test_labels, predictions)
print(f'Model precision is: {precScore*100}')

recallScore = recall_score(test_labels, predictions)
print(f'Model recall is: {recallScore*100}')

f1Score = f1_score(test_labels, predictions)
print(f'Model f1 score is: {f1Score*100}')

report = classification_report(test_labels, predictions)
print(f'Classification report:\n{report}')

# create a confusion matrix
cm = confusion_matrix(test_labels, predictions)
print(cm)

# save the trained model to the disk
file = open('trained_model.pkl', mode = 'wb')
pickle.dump(model, file)
file.close()