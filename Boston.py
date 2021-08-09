# imports

import numpy as np
# import matplotlib.pyplot as plt

import pandas as pd
# import seaborn as sns

# import warnings.filterwarnings('ignore')

from sklearn import preprocessing

# %matplotlib inline
import pickle

# importing the dataset

df = pd.read_csv("BostonHousing.csv")
df.drop(df.columns[[0]], axis=1, inplace=True)




# linear reg start

X = pd.DataFrame(np.c_[df['lstat'], df['rm'], df['ptratio']], columns = ['lstat','rm', 'ptratio'])
y = df['medv']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lm = LinearRegression(normalize=True).fit(X, y)

lm.fit(X_train, y_train)

predictions = lm.predict(X_test)


def predict_price(lstat,rm,ptratio):
    X_input = [[lstat, rm, ptratio]]
    prediction_input = lm.predict(X_input)
    return prediction_input

pickle.dump(lm, open('Boston.pkl', 'wb'))
# Loading model to compare the results
# model = pickle.load(open('model.pkl','rb'))
# print(lm.predict([[4.03, 7.185, 17.8]]))
