
"""
Spyder Editor

"""
name = input('Enter your name')
print(name) # prints the name
print(name[0]) # first letter of the name
print(name[1]) # second letter of the name
print(name[-1])# last letter of the name
print(name[0:3]) # prints the first 3 letter of name letter 0,1,2
print(name[2:]) # prints from the 3rd to the end
print(name[-5:]) # prints the last 5 letters
print(name[2:4])# prints the 3rd to 4th letter

print(name[0::2])# prints every other letter 
print(name[-1::-1]) # prints name in reverse

firstname = name.split('')[0] # splits from where the space charcter is and returns the first part of the name (first name)
lastname = name.split('')[1] # splits the name from space and returns last name

print(name.count('a')) # counts the numbers of letter 'a' in the name

#%% requesting user 5 names and then printing them
name =[]
for i in range(0,5):
    name.append(input("Please enter your first name: "))

print('Now printing the names')

for i in range(0,5):
    print(name[i])
    
#%% adding names together to make a long name
name =''
for i in range(0,5):
    name = name + input("Please enter your first name: ")
print(name)

#%% import numpy and rename it to np
import numpy as np # importing numpy and name it as 'np'

a = np.array([0,1,2,3,4,5,6,7,8,9]) # create numpy array with 10 elements

print(np.max(a)) # or you can use print(a.max())
print(np.min(a)) # or you can use print(a.min())
print(np.mean(a)) # or you can use print(a.mean())
print(a.shape) # printing the array shape

# Creating a python list with 5 elements
b = [1,2,3,4,5]
print(b)
b.append(6) # adding 6 to the end of the list
print(b)
# appending 100 more values to the end of the list
for i in range(0,100): # running the code blow for 100 times
    b.append(0) # adding 0 to the end of the array

c = np.array(b) # converting the list ot numpy array
print(type(b)) # Type of list b before conversion
print(type(c)) # type of the object after conversion


np.ones((1,1000))# Create a numpy array with 1000 elements of all ones (1)
np.zeros((1,1000)) # Create a numpy array with 1000 elements of all zeros (0)

# create a 2D numpy array
d = np.array([[1,2,3,4],[5,6,7,8]]) # crate a 2D array in format of [[row 1],[row 2],[row 3]...]
# The number of elements in each row defines the number of the columns
print(f'Shape of 2D array is: {d.shape}')
print(d.max())# maximum of the 2D array

print(d.max(axis=0))# prints the maximum of each column
print(d.max(axis=1))# prints the maximum of each row
print(d.mean(axis=0)) # mean/average each column of array
print(d.mean(axis=1)) # averages each row of the array

# reshape the numpy array
e = d.reshape((4,2)) # reshape the array from 2x4 to 4x2
print(e)
print(e.shape)
e = e.reshape((-1,1)) # flattening (making a column array)
print(e); print(e.shape)

e = e.reshape((2,4))# reshaping it to its original shape
print('\n')
# extracting the last column of the array
f = e[:,-1] # extracting the last column
print(f)

# adding the f to the last column of e
g = np.hstack((e,f.reshape((2,1))))
print(g)

# read a random file to python 

filePath = r'C:\Users\sho6\Downloads\\'
fileName = 'file.txt'
file = open(filePath + fileName,'r') # rading the txt file
lineData = file.readline() # reading each line of the file
print(f'there are {lineData.count("the")} instances of word "the"') # print counts of the word "the"
# put the code above in a for loop to do it for all the lines in the data. Do this yourself






