#we will be using y = mx + c
#the formula for finding m in linear regression is the following: ((mean x . mean y)- mean(x.y))/((mean x)^2 - mean(x^2))

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

def slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))
    c = (mean(ys) - (m * mean(xs)))
    return m,c

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)

m,c = slope_and_intercept(xs,ys)

regression_line = [(m*x)+c for x in xs]

plt.scatter(xs,ys,color='b')
plt.plot(xs, regression_line)
plt.show()
