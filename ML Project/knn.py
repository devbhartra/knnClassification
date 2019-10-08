import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.metrics import accuracy_score as acc_score
from sklearn.model_selection import train_test_split

# dataset = np.loadtxt("cat1.csv", delimiter=',',skiprows=1)

direc=os.fsencode('.')  #current directory
cnt=32  #32 csvs
for File in os.listdir(direc):  #each file in directory
    # print(File)
    filename=os.fsdecode(File)  #get filename
    if filename.endswith('.csv'):  #only if csv
        # print(filename)
        dataset = np.loadtxt(filename, delimiter=',',skiprows=1)    #load into 2d numpy array, skip first row containing column labels
        if dataset.shape[1]==38:    #for csvs containing 38 columns after fix
            X = np.concatenate((dataset[:,0:14],dataset[:,15:37]),axis=1)   #all columns except class and predicted columns
            y = dataset[:,14]   #class column
        else:   #for csvs containing 31 cols
            X = np.concatenate((dataset[:,0:13],dataset[:,14:30]),axis=1)
            y = dataset[:, 13]
            
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        from sklearn.preprocessing import StandardScaler
            
        sc_X = StandardScaler() #scale cols to similar ranges
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)

        from sklearn.neighbors import KNeighborsClassifier
        classifier = KNeighborsClassifier(n_neighbors=1)
        classifier.fit(X_train, y_train)

        y_pred = classifier.predict(X_test)

        acc = acc_score(y_test, y_pred)
        print(acc * 100, filename)