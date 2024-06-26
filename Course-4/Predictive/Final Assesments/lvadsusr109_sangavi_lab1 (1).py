# -*- coding: utf-8 -*-
"""LVADSUSR109_Sangavi_Lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dB58blpYtUOUrLwte_vI4wXkkjByb-Zt
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score,LeaveOneOut
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix , classification_report,mean_squared_error,r2_score,accuracy_score,precision_score,recall_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import LeavePOut, cross_val_score
from sklearn.model_selection import ShuffleSplit, cross_val_score



df=pd.read_csv("/content/drive/MyDrive/Predictive/Final/loan_approval.csv")

print(df.head())

#EDA
df.info()
df.describe()

# check for missing values
print(df.isnull().sum())
print(df.duplicated().sum()) # No duplicate records

encoder=LabelEncoder()
df[' education']=encoder.fit_transform(df[' education'])
df[' self_employed']=encoder.fit_transform(df[' self_employed'])
df[' loan_status']=encoder.fit_transform(df[' loan_status'])

X=df.drop(columns=[' loan_status','loan_id'])
y=df[' loan_status']

corr=df.corr()
sns.heatmap(corr,annot=True)

'''
Train Test Split
'''

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3) ## Split, do we need specifiy ranam state??

'''
Classification
'''
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train,Y_train)
rf_predictions = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(Y_test, rf_predictions)
print("Random Forest Classifier Accuracy:", rf_accuracy)
accuracy = accuracy_score(Y_test, rf_predictions)
precision = precision_score(Y_test, rf_predictions, average='weighted')
recall = recall_score(Y_test, rf_predictions, average='weighted')
f1 = f1_score(Y_test, rf_predictions, average='weighted')
conf_matrix = confusion_matrix(Y_test, rf_predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)

# XGBOOST Classifier
xg_classifier = XGBClassifier()
xg_classifier.fit(X_train,Y_train)
xg_predictions = xg_classifier.predict(X_test)
xg_accuracy = accuracy_score(Y_test, xg_predictions)
print("Random Forest Classifier Accuracy:", xg_accuracy)
accuracy2 = accuracy_score(Y_test, xg_predictions)
precision = precision_score(Y_test, xg_predictions, average='weighted')
recall = recall_score(Y_test, xg_predictions, average='weighted')
f1 = f1_score(Y_test, xg_predictions, average='weighted')
conf_matrix = confusion_matrix(Y_test, xg_predictions)

print("Accuracy:", accuracy2)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)

sns.barplot([accuracy,accuracy2])