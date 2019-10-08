#uses the std libraries but will work only for one file
#Using Min Max scaler to scale b/w 0 and 1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc_score

dataset = np.loadtxt('cat1_test.csv', delimiter=',')    #load into 2d numpy array, skip first row containing column labels
if dataset.shape[1]==38:    #for csvs containing 38 columns after fix
    X = np.concatenate((dataset[:,0:14],dataset[:,15:37]),axis=1)   #all columns except class and predicted columns
    y = dataset[:,14]   #class column
else:   #for csvs containing 31 cols
    X = np.concatenate((dataset[:,0:13],dataset[:,14:30]),axis=1)
    y = dataset[:, 13]
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc_X = MinMaxScaler(feature_range=(0, 1)) #scale cols to similar ranges
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#here I have to implement my own logic

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=6,weights='distance')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

acc = acc_score(y_test, y_pred)
print(acc * 100)