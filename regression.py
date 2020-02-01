#regression is used for supervised learning for continuous data
#find a model to fit data

import quandl, math
import numpy as np #numpy module to convert data to numpy arrays, which is what Scikit-learn wants.
import pandas as pd
from sklearn import preprocessing, svm, model_selection
#preprocessing is used for feature scaling
#cross validation is used to split the dataset intp testing and training
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL") #getting the data for the google stock

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']] #we are choosing the features that we want

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0 #creates a new column in our dataframe
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True) #this is how we will handle missing data
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1)) #our features are everything except label
y = np.array(df['label'])

X = preprocessing.scale(X) #feature scaling on our features

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) #20 percent of data is the test data
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)
