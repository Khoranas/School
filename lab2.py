import numpy as np
import pandas as pd
import pickle

# Reading raw_text.txt and print the first word in each line
filePath = 'raw_text.txt'
file = open(filePath, mode='rt') # opening the file as read-only text mode='rt'

lines = [] # create an empty array to hold every line of the data
firstWords = [] # create an emprty array to hold first word of every line
while True: # create an infinite loop to read as long as there are lines in data
    
    lineData = file.readline() # reads one line at a time.
    if not lineData: # if the line is empty it means we reached end of the file and stop the loop
        break # stops the loop
    lines.append(lineData) # add the text from each line to the list "lines"
    word = lineData.split(' ')[0] # split all the spaces and grab the first element
    firstWords.append(word) # add the word from each line to the list "firstWords"
    
# print all the first words that has been extracted.
for item in firstWords:
    print(item)

input('Exercise 1.A is complete. Press Enter to go to the next Exercise.\n')
%reset -sf
filePath = 'sampleCSV.csv'
dataframe= pd.read_csv(filePath) # reading the csv file with pandas
arraydata = dataframe.to_numpy() # converting from dataframe to numpy array
print(arraydata.max()) # maximum of the data
print(arraydata.min()) # minimum of the data
print(arraydata.shape) # shape of the array
print(arraydata.shape[0]) # number of the rows in the data
print(arraydata.shape[1]) # number of hte columns in the data

input('Exercise 1.B is complete. Press Enter to go to the next Exercise.\n')
%reset -sf

filePath = 'sampleExcel.xlsx'
dataframe = pd.read_excel(filePath) # reading excel file with pandas read_excel()
arraydata = dataframe.to_numpy() # convert dataframe to numpy
print(arraydata.max()) # maximum of the data
print(arraydata.min()) # minimum of the data
print(arraydata.shape) # shape of the array
print(arraydata.shape[0]) # number of the rows in the data
print(arraydata.shape[1]) # number of hte columns in the data

input('Exercise 1.C is complete. Press Enter to go to the next Exercise.\n')

%reset -sf

filePath = 'samplePickle.pkl'
file = open(filePath, 'rb') # open a binary read-only file
data = pickle.load(file) # load the data to python
print(type(data)) # printing type of the data
# now we know the type of the data and we use appropriate function to find its size/shape
print(len(data)) # because type of the data is a list we use len if it was numpy array we use shape
print(data[0]) # print the value of the first element in the data
print(data[-1]) # print the value of the last element in the data
# convert data to numpy array to find its min and max
newData = np.array(data) # convert data to numpy array
print(newData.max()) # print maximum value of data
print(newData.min()) # print minimum value of data

input('Exercise 1.D is complete. Press Enter to go to the next Exercise.\n')


%reset -sf
# useing to_csv()
data = np.random.rand(50,30) # create random dataset
dataframe = pd.DataFrame(data) # convert from numpy array to dataframe
newFileName = 'my_csv_dataset.csv' # defining the file name
dataframe.to_csv(newFileName, header=False, index=False) # writing CSV format to disk
print('Dataset saved as CSV.')

# using to_excel()
data = np.random.rand(50,30) # create random dataset
dataframe = pd.DataFrame(data) # convert from numpy array to dataframe
newFileName = 'my_excel_dataset.xlsx' # defining the file name
dataframe.to_excel(newFileName, header=False, index=False) # writing excel format to disk
print('Dataset saved as Excel\n')
print('Finished writing dataset to disk. You should now have 2 files created.')
print('Check the disk to see if you can find the files. Try to open them and see their content in notepad and excel\n')

input('Exercise 2.A is complete. Press Enter to go to the next Exercise.\n')

# creating a sample pickle file
data = list(np.random.randint(0,100,10000))  # create a sample data
newFileName = 'my_pickle_dataset.pkl'
file = open(newFileName, 'wb') # open a binary file to write to
pickle.dump(data,file) # write to the opened file
file.close() # close the file after writing
print('Dataset saved as Pickle')

input('Exercise 2.B is complete. Press Enter to go to the next Exercise.\n')
print('This is the end of the exercises.')




