# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('data.csv')

dataset['Ag'].fillna(0, inplace=True)
dataset['Au'].fillna(0, inplace=True)
dataset['Cd'].fillna(0, inplace=True)
dataset['Co'].fillna(0, inplace=True)
dataset['Cu'].fillna(0, inplace=True)
dataset['Fe'].fillna(0, inplace=True)
dataset['Mn'].fillna(0, inplace=True)
dataset['Ni'].fillna(0, inplace=True)
dataset['Pb'].fillna(0, inplace=True)

# dataset['Zn'].fillna(dataset['Zn'].mean(), inplace=True)

X = dataset.iloc[:, :9]

 
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6,5,7,5,4,6,5]]))