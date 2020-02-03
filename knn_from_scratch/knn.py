import numpy as np
from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def knn(data, predict, k=3):
    distances = [] #store all the euclidean distances from predict point to the all points in dataset O(n)
    for group in data:
        for features in data[group]:
            euclidean_distance = np.sqrt(np.sum(np.array(features)-np.array(predict))**2)
            distances.append([euclidean_distance,group])

    #the distances list will look like :: [[1,r], [3,k] ...]
    print(distances)

    votes = [i[1] for i in sorted(distances)[:k]] #get the first k points that are closest to the new point
    return Counter(votes).most_common(1)[0][0] #return the most common element

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]

for i in dataset:
    for z in dataset[i]:
        plt.scatter(z[0],z[1],s=100,color=i)

result = knn(dataset, new_features)
plt.scatter(new_features[0], new_features[1], marker= "x" ,s=100, color = result)
plt.show()
