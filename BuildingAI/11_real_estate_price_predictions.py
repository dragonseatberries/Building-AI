# introduction to linear regression
# predicting the output of data given the data set and the coefficients of the linear regression

import numpy as np
X = [[66, 5, 15, 2, 500],
     [21, 3, 50, 1, 100],
     [120, 15, 5, 2, 1200]]         # data
c = [3000, 200, -50, 5000, 100]     # coefficient values


def predict(X, c):
    for i in range(len(X)):  # loop through all data points in X data set
        # for each data point calculate the prediction
        cx = [c * x for c, x in zip(c, X[i])]
        print(sum(cx))


predict(X, c)

# condensed numpy approach
x = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100]])
c = np.array([3000, 200, -50, 5000, 100])

print(x @ c)
