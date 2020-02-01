#KNN is a classification algorithm where you basically have a datapoint and want to classify what group it is in based on what group it is closest to in euclidean distance
import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')#read in the dataset
df.replace('?',-99999, inplace=True)#account for null values 
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1)) #define our features
y = np.array(df['class']) #define our target variable

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1],[9,10,10,8,7,10,9,7,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)
print(prediction)
