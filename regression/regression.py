#regression is used for supervised learning for continuous data
#find a model to fit data

import quandl, math
import numpy as np #numpy module to convert data to numpy arrays, which is what Scikit-learn wants.
import pandas as pd
from sklearn import preprocessing, svm, model_selection
#preprocessing is used for feature scaling
#cross validation is used to split the dataset intp testing and training
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pickle

style.use('ggplot')

df = quandl.get("WIKI/GOOGL") #getting the data for the google stock

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']] #we are choosing the features that we want

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0 #creates a new column in our dataframe
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True) #this is how we will handle missing data
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) #20 percent of data is the test data
#clf = LinearRegression(n_jobs=-1) #n jobs is the number of jobs it can run in parallel, -1 means run as many as you can
#clf.fit(X_train, y_train)
#confidence = clf.score(X_test, y_test)

#we have now stored the model in a pickle file so that we dont have to retrain the classifier every single time we want to make a prediction

#with open('linearregression.pickle','wb') as f:
    #pickle.dump(clf, f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)



confidence = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately) #making predictions for 30 days
print(forecast_set, confidence, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
