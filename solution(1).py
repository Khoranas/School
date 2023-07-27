import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# This lab is uses unsupervised dataset. This is the first unsupervised model we are using
#  the dataset has no class labels. as it is unsupervised, we do not have any means of testing the model 
# because we cant test the model we do not split the data into train and test either.
data = pd.read_excel('Excelrates-GBP-USD.xlsx')# read dataset! Pay attention because the file is excel we used pd.read_excel()
data = np.array(data)# data.to_numpy() # converting to numpy using your prefered method

rate = data[:, -1] # the dataset for this lab has only one useful feature, and thats the rates
# data = np.reshape(data,(-1,1))
# We need to reshape the rates so that it will be 2 dimensional. scikilearn models require the features to be 2D.
# They need to be 2D because that's how sickilearn models can distinguish between the number of samples(datapoints)and number of features
rate = rate.reshape((-1,1)) 

print(np.std(rate)) # calculating the standard deviation of the rates
print(np.mean(rate)) # calculating the average/mean of the rates

# create an isolation forest model
# When making the model we initialize it with contamination=2% or 0.02
# Contamination is an estimate of how many anomalies are in the dataset, our anomalies always should be much smaller than the normal samples
# bootstrap is a method of resampling the data for ensemple learning models which we have set to True
model = IsolationForest(contamination = 0.02, bootstrap=True)
model.fit(rate) # training the model
predict = model.predict(rate) # getting the predictions from the model
# "predict" is an array that has the same size as the rate, For each sample we have a prediction as whether or not it is normal or anomalous
#  By definition of the scikilearn, the normal samples are identified by 1 and anomalies are coded by -1
print(np.sum(predict))# calculating the sum of the predictions


abLoc = np.where(predict == -1)[0] # finding the total number of the anomalies that are detected
year = np.linspace(2021,1999, np.shape(rate)[0]) # creating a variable that represents our years

abNormYears = np.floor(year[abLoc]) # getting rid of the months of the year, we only want the year not months or day
print(np.unique(abNormYears)) # getting rid of the repeated anomalies in the same year, just see them once
# Now you should be able to see the anomalies. What do you think about the year that the anomalies in the exchange rate has happened?
# you should see [2007. 2016 2019]. 2007 was the financial crysis or gerat recession. 2016 was when the brexit was voted. and 2019 was the pandemic

# Here you can plot the rates and also add the anomalies on top of them to see them all
plt.plot(year, rate)
plt.plot(year[abLoc],rate[abLoc],marker='x',linestyle='')
plt.xlabel('Years, from 1999 to 2021')
plt.ylabel('GPB-USD ex-rates')
plt.legend(['Data (ex-rate)', 'Anomalies'])






