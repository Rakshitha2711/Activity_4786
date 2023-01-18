# -*- coding: utf-8 -*-
"""Activity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X1mM3yR894vm139-BoUIQvVdoLJDAoV4
"""

import pandas as pd
import numpy as np

data = pd.read_excel("Bank_Personal_Loan_Modelling.xlsx")

data.shape

data.size

data.head(5)

data.tail(5)

data.isnull().sum()

data.info()

data.nunique()

categorical_variables=[col for col in data.columns if data[col].nunique()<=5]
print(categorical_variables)
continuous_variables=[col for col in data.columns if data[col].nunique()>5]
print(continuous_variables)

data.dtypes

cat_attr =(['Family', 'Education', 'Personal Loan', 'Securities Account', 'CD Account', 'Online', 'CreditCard'])
for col in cat_attr:
  data[col] = data[col].astype('category')

data.dtypes

data.drop(['ID','ZIP Code'],axis=1,inplace=True)

from sklearn.model_selection import train_test_split

y = data["Personal Loan"]
X = data.drop(["Personal Loan"],axis=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=123)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


"""Logistic Reegression"""

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train,y_train)

X_train_pred = lr.predict(X_train)
X_test_pred = lr.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_train,X_train_pred)

accuracy_score(y_test,X_test_pred)

"""Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier

DT = DecisionTreeClassifier()

DT.fit(X_train,y_train)

X_train_pred = DT.predict(X_train)
X_test_pred = DT.predict(X_test)

accuracy_score(y_train,X_train_pred)

accuracy_score(y_test,X_test_pred)

import pickle 
pickle.dump(lr,open('model.pkl','wb'))
model =pickle.load(open('model.pkl','rb'))
